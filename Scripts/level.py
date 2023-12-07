'''In this file implement all game logic'''

import pygame
from Scripts.tiles import Tile
from Scripts.settings import tile_size
from Scripts.settings import screen_height
from Scripts.player import Player


class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0 #
        self.world_shift_y = 0
    def scroll (self):
        player = self.player_tiles.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        direction_y = player.direction.y

        # Scroll world left and right
        if player_x < 50 and direction_x < 0:
            self.world_shift_x = 8
            player.speed = 0
        elif player_x > 1000 and direction_x > 0:
            self.world_shift_x = -8
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 8

        # Scroll world up and down
        if player_y < 50 and direction_y < 0:
            self.world_shift_y = 8
            player.speed = 0
        elif player_y > screen_height - 50 and direction_y > 0:
            self.world_shift_y = -8
            player.speed = 0
        else:
            self.world_shift_y = 0
            player.speed = 8

    # setup_level create level from a list.
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player_tiles = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout): # loop thru a map list
            for column_index, column in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size

                if column == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    player_sprite = Player((x, y))
                    self.player_tiles.add(player_sprite)

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)

        # player
        self.player_tiles.update()
        self.player_tiles.draw(self.display_surface)
        self.scroll()

