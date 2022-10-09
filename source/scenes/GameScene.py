import pygame
from scenes.BaseScene import BaseScene
from objects.Player import Player
from objects.Ball import Ball
from objects.Pitch import Pitch
from objects.Score import Score
from utilities.constant import WHITE, RED, bluePositions, redPositions
import Box2D
from Box2D.b2 import world

class GameScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("GameScene", screen, sceneManager)
        self.blueTeam = []
        self.redTeam = []
        self.blueImage = {}
        self.redImage = {}
        self.barImage = {}
        self.keyUpList = []
        self.currentBluePlayerIndex = 0
        self.currentRedPlayerIndex = 0
        self.redScore = 0
        self.blueScore = 0
        self.redGoal = pygame.Rect(0, 305, 45, 190)
        self.blueGoal = pygame.Rect(955, 305, 45, 190)
        self.accelerate = 10000
        self.timelimit = 90
        self.isEnd = False
        self.__load()

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in self.events:
            if not self.isEnd:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.sceneManager.startScene("MenuScene")
                    if event.key == pygame.K_t:
                        self.__toggleBluePlayer()
                    if event.key == pygame.K_p:
                        self.__toggleRedPlayer()
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,
                    pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
                        self.keyUpList.append(event.key)
                elif event.type == pygame.USEREVENT:
                    self.decreaseTime()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.replayButton.get_rect(topleft = (400, 350)).collidepoint(x, y):
                        self.reset()
        
    def start(self):
        self.__createGameObjects()
        self.__createPhysicsWorld()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    def reset(self):
        self.blueTeam = []
        self.redTeam = []
        self.keyUpList = []
        self.currentBluePlayerIndex = 0
        self.currentRedPlayerIndex = 0
        self.redScore = 0
        self.blueScore = 0
        self.timelimit = 90
        self.isEnd = False
        self.__load()
        self.start()
    
    def decreaseTime(self):
        self.timelimit -= 1
        if self.timelimit == 0:
            pygame.time.set_timer(pygame.USEREVENT, 0)
            self.isEnd = True 
            
    def update(self, deltaTime):
        if not self.isEnd:
            self.__handleBlue()
            self.__handleRed()
            
            for player in self.blueTeam + self.redTeam:
                player.update(deltaTime)

            self.ball.update(deltaTime)
    
    def showEndGame(self):
        titleFont = pygame.font.Font('freesansbold.ttf', 40)
        titleSurf = titleFont.render('The match finished!', True, RED)
        titleRect = titleSurf.get_rect()
        titleRect.center = (500, 300)
        self.screen.blit(titleSurf, titleRect)
        self.replayButton = pygame.image.load("assets/images/replay.png")
        self.screen.blit(self.replayButton, (400, 350))

    def render(self):
        self.field.render(self.screen)
        self.ball.render(self.screen)
        self.score.render(self.screen, self.redScore, self.blueScore, self.timelimit)
        for player in self.blueTeam + self.redTeam:
            player.render(self.screen)
        if self.isEnd:
            self.showEndGame()

    def exit(self):
        self.screen.fill(WHITE)
        self.blueTeam.clear()
        self.redTeam.clear()
    

    def __load(self):
        self.fieldImg = pygame.image.load("assets/images/field_with_brick.png")
        self.ballImage = pygame.image.load("assets/images/ball.png")
        self.barImage = pygame.image.load("assets/images/bar.png")
        self.redImage['normal'] = pygame.image.load("assets/images/player1.png")
        self.redImage['active'] = pygame.image.load("assets/images/player1_active.png")
        self.blueImage['normal'] = pygame.image.load("assets/images/player0.png")
        self.blueImage['active'] = pygame.image.load("assets/images/player0_active.png")    
        self.kickSound = pygame.mixer.Sound("assets/sounds/kick.wav")
        self.voice = pygame.mixer.Channel(5)
        
    def __createPhysicsWorld(self):
        self.world = world(gravity=(0, 0), doSleep=False)
        
        self.ball.body = self.world.CreateDynamicBody(
            userData=self.ball,
            position=(self.ball.position.x, self.ball.position.y),
            linearDamping=0.3
        )

        self.ball.fixture = self.ball.body.CreateCircleFixture(radius=self.ball.radius-1, density=1, friction=0.3, restitution=0.8)

        self.ball.body.mass = 1

        for player in self.blueTeam + self.redTeam:
            player.body = self.world.CreateDynamicBody(
                userData=player,
                position=(player.position.x, player.position.y),
            )

            player.fixture = player.body.CreateCircleFixture(radius=player.radius, density=10, friction=0.3)

            player.body.mass = 30

        self.__createWalls()
        self.__createLeftGoal()
        self.__createRightGoal()
        
    def __createWalls(self):
        self.bottomWall = self.world.CreateStaticBody(
            position=(0, 768), 
            shapes=Box2D.b2PolygonShape(box=(1000, 32)),
        )

        self.topWall = self.world.CreateStaticBody(
            position=(0, 0), 
            shapes=Box2D.b2PolygonShape(box=(1000, 32)),
        )

        self.topLeftWall = self.world.CreateStaticBody(
            position=(0, 0), 
            shapes=Box2D.b2PolygonShape(box=(32, 285)),
        )

        self.topRightWall = self.world.CreateStaticBody(
            position=(968, 0), 
            shapes=Box2D.b2PolygonShape(box=(32, 285)),
        )

        self.bottomLeftWall = self.world.CreateStaticBody(
            position=(0, 782), 
            shapes=Box2D.b2PolygonShape(box=(32, 300)),
        )

        self.bottomRightWall = self.world.CreateStaticBody(
            position=(968, 782), 
            shapes=Box2D.b2PolygonShape(box=(32, 300)),
        )

    def __createLeftGoal(self):
        self.topWall = self.world.CreateStaticBody(
            position=(0, 253), 
            shapes=Box2D.b2PolygonShape(box=(16, 32)),
        )

        self.bottomWall = self.world.CreateStaticBody(
            position=(0, 782), 
            shapes=Box2D.b2PolygonShape(box=(16, 32)),
        )

        self.leftWall = self.world.CreateStaticBody(
            position=(-20, 253), 
            shapes=Box2D.b2PolygonShape(box=(1, 300)),
        )

    def __createRightGoal(self):
        self.topWall = self.world.CreateStaticBody(
            position=(968, 253), 
            shapes=Box2D.b2PolygonShape(box=(16, 32)),
        )

        self.bottomWall = self.world.CreateStaticBody(
            position=(968, 782), 
            shapes=Box2D.b2PolygonShape(box=(16, 32)),
        )

        self.rightWall = self.world.CreateStaticBody(
            position=(985, 253), 
            shapes=Box2D.b2PolygonShape(box=(1, 300)),
        )
    
    def createPlayers(self):
        for i in range(0, 3):
            self.blueTeam.append(Player(self.blueImage['normal'], self.blueImage['active'], bluePositions[i]))
            self.redTeam.append(Player(self.redImage['normal'], self.redImage['active'], redPositions[i]))
            self.redTeam[i].flip(True, None)
            
        self.blueTeam[self.currentBluePlayerIndex].active = True
        self.redTeam[self.currentRedPlayerIndex].active = True
    
    def resetPositions(self):
        for i in range(0, 3):
            self.blueTeam[i].setPosition(bluePositions[i])
            self.redTeam[i].setPosition(redPositions[i])
        self.ball.setPostion((484, 384))
        self.ball.body.linearVelocity.x = 0
        self.ball.body.linearVelocity.y = 0
        
    def __createGameObjects(self):
        self.createPlayers()

        self.field = Pitch(self.fieldImg, (0, 0))
        self.ball = Ball(self.ballImage, (484, 384))
        self.score = Score(self.barImage, (320, 5))
        
    def __toggleBluePlayer(self):
        self.blueTeam[self.currentBluePlayerIndex].active = False
        self.currentBluePlayerIndex += 1
        if self.currentBluePlayerIndex >= self.blueTeam.__len__():
            self.currentBluePlayerIndex = 0

        self.blueTeam[self.currentBluePlayerIndex].active = True

    def __toggleRedPlayer(self):
        self.redTeam[self.currentRedPlayerIndex].active = False
        self.currentRedPlayerIndex += 1
        if self.currentRedPlayerIndex >= self.redTeam.__len__():
            self.currentRedPlayerIndex = 0

        self.redTeam[self.currentRedPlayerIndex].active = True

    def __handleBlue(self):
        currentPlayer = self.blueTeam[self.currentBluePlayerIndex]
        self.checkCollision(currentPlayer)
        
        if self.pressedKeys[pygame.K_w]:
            currentPlayer.flip(None, 1)
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,-currentPlayer.body.mass * self.accelerate), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_d]:
            currentPlayer.flip(-1, None)
            currentPlayer.body.ApplyLinearImpulse(impulse=(currentPlayer.body.mass * self.accelerate, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_a]:
            currentPlayer.flip(1, None)
            currentPlayer.body.ApplyLinearImpulse(impulse=(-currentPlayer.body.mass * self.accelerate, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_s]:
            currentPlayer.flip(None, -1)
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,currentPlayer.body.mass * self.accelerate), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)

        if not (self.pressedKeys[pygame.K_w] or self.pressedKeys[pygame.K_s]):
            currentPlayer.body.linearVelocity.y = 0

        if not (self.pressedKeys[pygame.K_d] or self.pressedKeys[pygame.K_a]):
            currentPlayer.body.linearVelocity.x = 0

        for i in range(0, self.blueTeam.__len__()):
            if i != self.currentBluePlayerIndex:
                self.blueTeam[i].body.linearVelocity.x = 0
                self.blueTeam[i].body.linearVelocity.y = 0

        self.calculateScore(False)

    def __handleRed(self):
        currentPlayer = self.redTeam[self.currentRedPlayerIndex]
        self.checkCollision(currentPlayer)
        
        if self.pressedKeys[pygame.K_UP]:
            currentPlayer.flip(None, 1)
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,-currentPlayer.body.mass * self.accelerate), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_RIGHT]:
            currentPlayer.flip(-1, None)
            currentPlayer.body.ApplyLinearImpulse(impulse=(currentPlayer.body.mass * self.accelerate, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_LEFT]:
            currentPlayer.flip(1, None)
            currentPlayer.body.ApplyLinearImpulse(impulse=(-currentPlayer.body.mass * self.accelerate, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_DOWN]:
            currentPlayer.flip(None, -1)
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,currentPlayer.body.mass * self.accelerate), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)

        if not (self.pressedKeys[pygame.K_UP] or self.pressedKeys[pygame.K_DOWN]):
            currentPlayer.body.linearVelocity.y = 0

        if not (self.pressedKeys[pygame.K_RIGHT] or self.pressedKeys[pygame.K_LEFT]):
            currentPlayer.body.linearVelocity.x = 0

        for i in range(0, self.redTeam.__len__()):
            if i != self.currentRedPlayerIndex:
                self.redTeam[i].body.linearVelocity.x = 0
                self.redTeam[i].body.linearVelocity.y = 0
        
        self.calculateScore(True)
        
    def calculateScore(self, isRed):
        if isRed:
            if pygame.Rect.collidepoint(self.redGoal, self.ball.getX(), self.ball.getY()):
                self.redScore += 1
                self.resetPositions()
        else:
            if pygame.Rect.collidepoint(self.blueGoal, self.ball.getX(), self.ball.getY()):
                self.blueScore += 1
                self.resetPositions()
    
    def checkCollision(self, actor):
        ballCircle = pygame.draw.circle(self.screen, (0, 0, 0), (self.ball.position.x + 16, self.ball.position.y + 16), 15)
        playerCircle = pygame.draw.circle(self.screen, (0, 0, 0), (actor.position.x + 25, actor.position.y + 25), 25)
        if ballCircle.colliderect(playerCircle):
            if not self.voice.get_busy():
                self.voice.play(self.kickSound)