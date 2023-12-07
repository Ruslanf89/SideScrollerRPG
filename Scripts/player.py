import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = position)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8 #
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.x = 0
            self.direction.y = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        self.x = self.rect.centerx
        self.y = self.rect.centery