'''This is a main file for SideScrollerRPG game project
Main game loop will be here
RUN this file for play the game
'''

import pygame, sys
from Scripts.settings import *
from Scripts.level import Level
from Scripts.level_map import level_0
# import Scripts.player

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SideScrollerRPG')
clock = pygame.time.Clock()
level = Level(level_0, screen)

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)

