'''This file contain all game settings attributes'''

from Scripts.level_map import *

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size # Make windows height change dynamicaly(depending on a map size)