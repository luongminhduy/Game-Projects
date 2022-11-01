import math
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
        Cuirass.collected_amount = 0
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
                    if row_index == 0: tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, "Dirt")
                    elif(layout[row_index - 1][col_index] != 'X'):
                        tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, "Grass")
                    else: tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, "Dirt")
                    self.tiles.add(tile)
                if cell == "E":
                    enemy = Enemy((col_index * tile_size, (row_index + 1) * tile_size))
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
        
        if player_x < tile_size * 5:
            self.world_shift = 0
            if player.rect.bottomleft[0] <= 0:
                player.rect.left = 0
                player.touch_left = True
            player.speed = player_speed  # type: ignore           
        elif player_x < screen_width / 4 and direction_x < 0:
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
                elif player.direction.x > 0:                   
                    player.rect.right = sprite.rect.left
                    player.touch_right = True
                    self.current_player_x = player.rect.right
        
        if player.touch_left and (player.rect.left < self.current_player_x or player.direction.x >=0):
            player.touch_left = False
            
        if player.touch_right and (player.rect.right > self.current_player_x or player.direction.x <=0):
            player.touch_right = False
                    
    def vertical_player_movement_collision(self):
        player = self.player.sprite            
        player.apply_gravity() 
        
        for sprite in self.tiles.sprites() + self.chests.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.touch_ceiling = True
                    break
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.touch_ground = True
                    player.direction.y = 0
                    break
                    
        if player.touch_ground and player.direction.y < 0 or player.direction.y > player.gravity:
            player.touch_ground = False
        
        if player.touch_ceiling and player.direction.y > 0:
            player.touch_ceiling = False
                
    def check_and_unlock_chest(self):
        player = self.player.sprite

        if player.using_key and Key.collected_amount > 0:           
            for chest in self.chests.sprites():
                if (player.rect.bottom == chest.rect.top) or abs(player.rect.left - chest.rect.right) <= 15 or abs(player.rect.right - chest.rect.left) <= 10:
                    chest.unlock()                   
                    Key.collected_amount -= 1
                    print('open')
                    break
                
        player.using_key = False

    def player_enemy_collision(self):
        player = self.player.sprite
        for enemy in self.enemies:
            if enemy.rect.colliderect(player.rect):
                if player.touch_ground == False and player.rect.bottom >= enemy.rect.top:
                    player.touch_ground = True
                    player.jump()
                    enemy.die()
                else:
                    hurt_fx.play()
                    enemyAttack_fx.play()
                    if player.wearing_cuirass:
                        if Cuirass.collected_amount > 0:
                            Cuirass.collected_amount -= 1
                        else: player.wearing_cuirass = False
                        player.jump()
                    else:                          
                        self.reset = True
                        self.running = "gameover"
                        game_over_fx.play()

    def player_boss_collision(self):
        player = self.player.sprite
        for boss in self.bosses:
            if boss.collideRect.colliderect(player.rect):
                if (boss.attack):
                    melee_fx.play()
                    if (player.rect.x <= boss.rect.x + 56 and not(boss.right_moving) or player.rect.x >= boss.rect.x and boss.right_moving):
                        hurt_fx.play()                      
                        if player.wearing_cuirass:
                            if Cuirass.collected_amount > 0:
                                Cuirass.collected_amount -= 1
                            else: 
                                player.wearing_cuirass = False
                            player.jump()                  
                        else:
                            self.reset = True
                            self.running = "gameover"
                            game_over_fx.play()
                elif player.direction.y > 0:
                    player.touch_ground = True
                    player.jump()
                    boss.hp -= 1
                    print(boss.hp)
                    if (boss.hp < 0):
                        boss.die()
                        self.running = "victory"
    
    def check_player_falling(self):
        player = self.player.sprite
        if (player.rect.y > screen_height + 100):
            print("Game Over")
            self.reset = True
            self.running = "gameover"
            game_over_fx.play()
