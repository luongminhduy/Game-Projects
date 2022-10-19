import pygame
from tiles import Tile
from config import *
from player import Player

class Level:
    def __init__(self, level_data, surface) -> None:
        self.world_shift = 0
        self.display_surface = surface
        self.setup_level(level_data)
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    tile = Tile((col_index * tile_size, row_index * tile_size), tile_size)
                    self.tiles.add(tile)
                elif cell == "P":
                    player = Player((col_index * tile_size, row_index * tile_size))
                    self.player.add(player)
    
    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
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
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    
    def vertical_player_movement_collision(self):
        player = self.player.sprite            
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    break
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.canJump = True
                    player.direction.y = 0
                    break
                    
                