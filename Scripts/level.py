'''In this file implement all game logic'''

import pygame
from Scripts.tiles import Tile, StaticTile
from Scripts.settings import tile_size, screen_width
# from Scripts.player import Player
# from Scripts.particles import ParticleEffect
from Scripts.support import import_csv_layout, import_cut_graphics

class Level:
    def __init__(self, level_data, surface):
        # Variables
        self.display_surface = surface
        self.world_shift = -5
        # Terrain variables
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('../SideScrollerRPG/Sprites/terain/main/main_location_tileset.png')
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)
        return sprite_group
    def run(self):
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)



