'''In this file implement all game logic'''

import pygame
from Scripts.tiles import Tile
from Scripts.settings import tile_size, screen_width
from Scripts.player import Player

class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0 # make map scroll "+" value move left -> right "-" value move right -> left


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
    def scroll_x(self):
        player = self.player_tiles.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player_tiles.sprite
        player.rect.x += player.direction.x * player.speed

        # check for collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right # collision on right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left # collision on left

    def vertical_movement_collision(self):
        player = self.player_tiles.sprite
        player.apply_gravity()

        # check for collision
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player_tiles.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player_tiles.draw(self.display_surface)


