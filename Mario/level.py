from tkinter.font import families
import pygame
from tiles import Tile
from config import *
from player import Player
from coin import *
from key import *
from chest import *

class Level:
    def __init__(self, level_data, surface) -> None:
        self.world_shift = 0
        self.display_surface = surface
        Coin.collected_amount = 0
        Key.collected_amount = 0
        self.setup_level(level_data)
        self.current_player_x = 0
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.coins = []
               
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    tile = Tile((col_index * tile_size, row_index * tile_size), tile_size)
                    self.tiles.add(tile)
                elif cell == "P":
                    player = Player((col_index * tile_size, row_index * tile_size))
                    self.player.add(player)
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
        
        #level chests
        self.chests.update(self.world_shift, self.display_surface, self.player.sprite)
        self.chests.draw(self.display_surface)
        
        #coins
        for coin in self.coins:
            coin.update(self.world_shift)
            coin.coins.draw(self.display_surface)
        
        #player
        self.player.update()
        self.horizontal_player_movement_collision()
        self.vertical_player_movement_collision()
        self.player.draw(self.display_surface)
        self.scoll_x()               
        
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
                