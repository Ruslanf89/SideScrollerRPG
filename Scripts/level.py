'''In this file implement all game logic'''

import pygame
from Scripts.tiles import Tile
from Scripts.settings import tile_size


class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 1

    # setup_level create level from a list.
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout): # loop thru a map list
            for column_index, column in enumerate(row):
                if column == 'X':
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

class Player(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()

        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))  # Червоний колір для гравця
        self.rect = self.image.get_rect(topleft=position)

        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.velocity)

    def move(self, direction):
        if direction == "LEFT":
            self.velocity.x = -5
        elif direction == "RIGHT":
            self.velocity.x = 5
        elif direction == "UP":
            self.velocity.y = -5
        elif direction == "DOWN":
            self.velocity.y = 5
        else:
            self.velocity = pygame.Vector2(0, 0)