'''Tile class draw a map from a list that saved in level_map.py file'''

import pygame

# Tile class implementing map generation from a list
class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()

        self.image = pygame.Surface((size, size)) # (size, size) because rectangle created
        self.image.fill((0, 190, 0))
        self.rect = self.image.get_rect(topleft=position)
    def update(self, x_shift):
        self.rect.x += x_shift # Scroll thru the map
