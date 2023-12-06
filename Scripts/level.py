'''In this file implement all game logic'''

import pygame
from Scripts.tiles import Tile
from Scripts.settings import tile_size
from Scripts.player import Player

class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 1 # make map scroll "+" value move left -> right "-" value move right -> left

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
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player_tiles.update()
        self.player_tiles.draw(self.display_surface)

