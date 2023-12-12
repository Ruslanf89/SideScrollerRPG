import pygame
from Scripts.support import import_folder
from Scripts.settings import screen_width, screen_height
class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        # Player movements
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # Animation management
        self.last_update = pygame.time.get_ticks()

    def import_assets(self):
        character_path = 'C:/Users/Dypko/SideScrollerRPG/Sprites/character/'
        self.animations = {'Idle': [], 'Running': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_iput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_iput()
