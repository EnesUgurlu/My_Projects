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
map_to_list = []
with open(map, 'r') as file:
	for line in file:
		map_to_list.append(line.strip())

map_width = len(map_to_list[0]) * TILESIZE
map_height = len(map_to_list) * TILESIZE

