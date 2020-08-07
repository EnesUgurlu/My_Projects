import pygame

clock = pygame.time.Clock()
TILESIZE = 32
WIDTH = 24 * TILESIZE
HEIGHT = 16 * TILESIZE
PLAYER = pygame.image.load('Images/Cowboy_Dino.png')
WALL = pygame.image.load('Images/Wall_1.png')
GRASS = pygame.image.load('Images/Grass.png')
EMPTY = pygame.image.load('Images/Empty.png')
list_of_walls = []
list_of_grass = []
map = 'map_1.txt'
