import pygame
from scenes.BaseScene import BaseScene
from objects.Player import Player
from objects.Ball import Ball
from objects.Pitch import Pitch
from utilities.constant import WHITE

import Box2D
from Box2D.b2 import world

class GameScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("GameScene", screen, sceneManager)
        self.blueTeam = []
        self.redTeam = []
        self.blueImage = []
        self.redImage = []
        self.keyUpList = []
        self.currentBluePlayerIndex = 0
        self.currentRedPlayerIndex = 0
        self.force = 3000
        self.__load()

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    self.sceneManager.startScene("MenuScene")
                if event.key == pygame.K_t:
                    self.__toggleBluePlayer()
                if event.key == pygame.K_p:
                    self.__toggleRedPlayer()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.keyUpList.append(pygame.K_w)
                if event.key == pygame.K_s:
                    self.keyUpList.append(pygame.K_s)
                if event.key == pygame.K_a:
                    self.keyUpList.append(pygame.K_a)
                if event.key == pygame.K_d:
                    self.keyUpList.append(pygame.K_d)

                if event.key == pygame.K_UP:
                    self.keyUpList.append(pygame.K_UP)
                if event.key == pygame.K_DOWN:
                    self.keyUpList.append(pygame.K_DOWN)
                if event.key == pygame.K_RIGHT:
                    self.keyUpList.append(pygame.K_RIGHT)
                if event.key == pygame.K_LEFT:
                    self.keyUpList.append(pygame.K_LEFT)
            

    def start(self):
        self.__createGameObjects()
        self.__createPhysicsWorld()

    def update(self, deltaTime):
        self.__handleBlue()
        self.__handleRed()

        for player in self.blueTeam + self.redTeam:
            player.update(deltaTime)

        self.ball.update(deltaTime)
       

    def render(self):
        self.field.render(self.screen)
        self.ball.render(self.screen)

        for player in self.blueTeam + self.redTeam:
            player.render(self.screen)


        
    def exit(self):
        print("exit GameScene")
        self.screen.fill(WHITE)
    

    def __load(self):
        self.fieldImg = pygame.image.load("assets/images/field_with_brick.png")
        self.ballImage = pygame.image.load("assets/images/ball.png")
        bluePositions = [(250, 200), (250, 575), (100, 375)]
        redPositions = [(725, 200), (725, 575), (875, 375)]

        for i in range(0, 3):
            bluePlayerImage = pygame.image.load("assets/images/player0.png")
            blueActive = pygame.image.load("assets/images/player0_active.png")
            redPlayerImage = pygame.image.load("assets/images/player1.png")
            redActive = pygame.image.load("assets/images/player1_active.png")
            self.blueImage.append([bluePlayerImage, blueActive, bluePositions[i]])
            self.redImage.append([redPlayerImage, redActive, redPositions[i]])       

    def __createPhysicsWorld(self):
        self.world = world(gravity=(0, 0), doSleep=True)
        
        self.ball.body = self.world.CreateDynamicBody(
            userData=self.ball,
            position=(self.ball.position.x, self.ball.position.y),
            linearDamping=0.3
        )

        self.ball.fixture = self.ball.body.CreateCircleFixture(radius=self.ball.radius-1, density=1, friction=0.3, restitution=0.8)

        self.ball.body.mass = 2

        for player in self.blueTeam + self.redTeam:
            player.body = self.world.CreateDynamicBody(
                userData=player,
                position=(player.position.x, player.position.y),
            )

            player.fixture = player.body.CreateCircleFixture(radius=player.radius, density=10, friction=0.3)

            player.body.mass = 50

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

    def __createGameObjects(self):
        for i in range(0, 3):
            self.blueTeam.append(Player(self.blueImage[i][0], self.blueImage[i][1], self.blueImage[i][2]))
            self.redTeam.append(Player(self.redImage[i][0], self.redImage[i][1], self.redImage[i][2]))
            self.redTeam[i].flip(True, False)
            

        self.blueTeam[self.currentBluePlayerIndex].active = True
        self.redTeam[self.currentRedPlayerIndex].active = True

        self.field = Pitch(self.fieldImg, (0, 0))
        self.ball = Ball(self.ballImage, (484, 384))

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

        if self.pressedKeys[pygame.K_w]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,-currentPlayer.body.mass * self.force), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_d]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(currentPlayer.body.mass * self.force, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
            currentPlayer.flip(False, False)
        if self.pressedKeys[pygame.K_a]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(-currentPlayer.body.mass * self.force, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
            currentPlayer.flip(True, False)
        if self.pressedKeys[pygame.K_s]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,currentPlayer.body.mass * self.force), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)

        if not (self.pressedKeys[pygame.K_w] or self.pressedKeys[pygame.K_s]):
            currentPlayer.body.linearVelocity.y = 0

        if not (self.pressedKeys[pygame.K_d] or self.pressedKeys[pygame.K_a]):
            currentPlayer.body.linearVelocity.x = 0

        for i in range(0, self.blueTeam.__len__()):
            if i != self.currentBluePlayerIndex:
                self.blueTeam[i].body.linearVelocity.x = 0
                self.blueTeam[i].body.linearVelocity.y = 0


    def __handleRed(self):
        currentPlayer = self.redTeam[self.currentRedPlayerIndex]

        if self.pressedKeys[pygame.K_UP]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,-currentPlayer.body.mass * self.force), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_RIGHT]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(currentPlayer.body.mass * self.force, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_LEFT]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(-currentPlayer.body.mass * self.force, 0), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)
        if self.pressedKeys[pygame.K_DOWN]:
            currentPlayer.body.ApplyLinearImpulse(impulse=(0,currentPlayer.body.mass * self.force), point=(currentPlayer.position.x,currentPlayer.position.y), wake=True)

        if not (self.pressedKeys[pygame.K_UP] or self.pressedKeys[pygame.K_DOWN]):
            currentPlayer.body.linearVelocity.y = 0

        if not (self.pressedKeys[pygame.K_RIGHT] or self.pressedKeys[pygame.K_LEFT]):
            currentPlayer.body.linearVelocity.x = 0

        for i in range(0, self.redTeam.__len__()):
            if i != self.currentRedPlayerIndex:
                self.redTeam[i].body.linearVelocity.x = 0
                self.redTeam[i].body.linearVelocity.y = 0