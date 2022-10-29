from tkinter.font import families
from tkinter.tix import DirTree
import pygame
from boss import Boss
from tiles import Tile
from config import *
from player import Player
from coin import *
from key import *
from chest import *
from enemy import Enemy

class Level:
    def __init__(self, level_data, surface) -> None:
        self.world_shift = 0
        self.display_surface = surface
        Coin.collected_amount = 0
        Key.collected_amount = 0
        self.setup_level(level_data)
        self.current_player_x = 0
        self.running = "playing"
        self.reset = False
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coins = []
               
        self.bosses =  pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    if(layout[row_index - 1][col_index] != 'X'):
                        tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, "Grass")
                    else: tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, "Dirt")
                    self.tiles.add(tile)
                if cell == "E":
                    enemy = Enemy((col_index * tile_size, row_index * tile_size ))
                    self.enemies.add(enemy)                    
                if cell == "P":
                    player = Player((col_index * tile_size, row_index * tile_size))
                    self.player.add(player)
                if cell == "T":
                    boss = Boss((col_index * tile_size, row_index * tile_size )) 
                    self.bosses.add(boss)       
                elif cell == "$":
                    coin = Coins((col_index * tile_size, row_index * tile_size))
                    self.coins.append(coin)
                elif cell == "K":
                    key = Key((col_index * tile_size, row_index * tile_size))
                    self.keys.add(key)
                elif cell == "C":
                    chest = Chest((col_index * tile_size, (row_index + 1) * tile_size))
                    self.chests.add(chest)
                    
        Coin.current_player = self.player.sprite
    
    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #keys
        self.keys.update(self.world_shift, self.player.sprite)
        self.keys.draw(self.display_surface)
        
        #chests
        self.chests.update(self.world_shift, self.display_surface, self.player.sprite)
        self.chests.draw(self.display_surface)
        
        #coins
        for coin in self.coins:
            coin.update(self.world_shift)
            coin.coins.draw(self.display_surface)

        #enemy
        self.enemies.update(self.world_shift)
        self.enemies.draw(self.display_surface)

        #boss
        self.bosses.update(self.world_shift)
        self.bosses.draw(self.display_surface)
        
        #player
        self.player.update()
        self.horizontal_player_movement_collision()
        self.vertical_player_movement_collision()
        self.player_enemy_collision()
        self.player_boss_collision()
        self.check_player_falling()
        self.player.draw(self.display_surface)
        self.check_and_unlock_chest()
        self.scoll_x()               

        #self.enemy.update()
        
    def scoll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx # type: ignore
        direction_x = player.direction.x  # type: ignore
        
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = player_speed
            player.speed = 0  # type: ignore
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = - player_speed
            player.speed = 0  # type: ignore
        else:
            self.world_shift = 0
            player.speed = player_speed  # type: ignore
            
    def horizontal_player_movement_collision(self):
        player = self.player.sprite            
        player.rect.x += player.direction.x * player.speed 

        for sprite in self.tiles.sprites() + self.chests.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.touch_left = True
                    self.current_player_x = player.rect.left
                    player.collided_sprite = sprite
                    if sprite in self.chests.sprites() and sprite.is_blocked:
                        print('collide_chest')
                        player.touch_left_chest = True
                        player.collided_chest = sprite
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.touch_right = True
                    self.current_player_x = player.rect.right
                    player.collided_sprite = sprite
                    if sprite in self.chests.sprites() and sprite.is_blocked:
                        print('collide_chest')
                        player.touch_right_chest = True
                        player.collided_chest = sprite
        
        if player.touch_left and (player.rect.left < self.current_player_x or player.direction.x >=0):
            player.touch_left = False
            player.collided_sprite = None
            player.collided_chest = None
            player.touch_left_chest = False
            
        if player.touch_right and (player.rect.right > self.current_player_x or player.direction.x <=0):
            player.touch_right = False
            player.collided_sprite = None
            player.collided_chest = None
            player.touch_right_chest = False
                    
    def vertical_player_movement_collision(self):
        player = self.player.sprite            
        player.apply_gravity() 
        
        for sprite in self.tiles.sprites() + self.chests.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.touch_ceiling = True
                    player.collided_sprite = sprite
                    break
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.touch_ground = True
                    player.direction.y = 0
                    player.collided_sprite = sprite
                    if sprite in self.chests.sprites() and sprite.is_blocked:
                        player.on_chest = True
                        print('collide_chest')
                        player.collided_chest = sprite
                    break
                    
        if player.touch_ground and player.direction.y < 0 or player.direction.y > player.gravity:
            player.touch_ground = False
            player.collided_sprite = None
            player.collided_chest = None
            player.on_chest = False
        
        if player.touch_ceiling and player.direction.y > 0:
            player.touch_ceiling = False
            player.collided_sprite = None
                
    def check_and_unlock_chest(self):
        player = self.player.sprite

        # if player.using_key and Key.collected_amount > 0:           
        #     for chest in self.chests.sprites():
        #         print("chest right:",chest.rect.right )
        #         print("player left:", player.rect.left)
        #         print("chest left:",chest.rect.left )
        #         print("player right:", player.rect.right)
        #         if (player.rect.bottom == chest.rect.top) or (player.rect.left == chest.rect.right) or (player.rect.right == chest.rect.left):
        #             chest.unlock()                   
        #             Key.collected_amount -= 1
        #             print('open')
        #             break
        if player.using_key and Key.collected_amount > 0: 
            if player.collided_chest != None:
                player.collided_chest.unlock()
                Key.collected_amount -= 1
                print('open') 
                player.collided_chest = None
                    
                
            
        player.using_key = False

    def player_enemy_collision(self):
        player = self.player.sprite
        for enemy in self.enemies:
            if enemy.rect.colliderect(player.rect):
                if player.direction.y > 1:
                    print(player.direction.y)
                    player.touch_ground = True
                    player.jump()
                    enemy.die()
                else:
                    self.reset = True
                    self.running = "gameover"

    def player_boss_collision(self):
        player = self.player.sprite
        for boss in self.bosses:
            if boss.collideRect.colliderect(player.rect):
                if (boss.attack):
                    print("Game Over")
                    self.reset = True
                    self.running = "gameover"
                elif player.direction.y > 0:
                    player.touch_ground = True
                    player.jump()
                    boss.hp -= 1
                    print(boss.hp)
                    if (boss.hp < 0):
                        boss.die()
    
    def check_player_falling(self):
        player = self.player.sprite
        if (player.rect.y > screen_height + 100):
            print("Game Over")
            self.reset = True
            self.running = "gameover"
