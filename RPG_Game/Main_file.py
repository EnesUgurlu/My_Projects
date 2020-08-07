import pygame
import sys
from pygame.locals import *

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
map = 'map_2.txt'


class Player:
	def __init__(self, game, x, y):
		self.game = game
		self.x = x * TILESIZE
		self.y = y * TILESIZE

	def spawn(self):
		main_screen.blit(PLAYER, (self.x, self.y))

	def event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					self.move(dx=1)
				if event.key == K_LEFT:
					self.move(dx=-1)
				if event.key == K_UP:
					self.move(dy=-1)
				if event.key == K_DOWN:
					self.move(dy=1)

	def move(self, dx=0, dy=0):
		self.event()
		if not self.collision(dx, dy):
			self.x += dx * TILESIZE
			self.y += dy * TILESIZE

	def collision(self, dx=0, dy=0):
		for wall in list_of_walls:
			if wall.rect.x == self.x + dx * TILESIZE and \
					wall.rect.y == self.y + dy * TILESIZE:
				return True
		return False

class Wall:
	def __init__(self, game, x, y):
		self.x = x
		self.y = y
		self.game = game
		self.image = WALL
		self.rect = self.image.get_rect()
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE
		main_screen.blit(self.image, (self.rect.x, self.rect.y))

class Tile:
	def __init__(self, game, x, y):
		self.x = x
		self.y = y
		self.game = game
		self.image = EMPTY
		self.rect = self.image.get_rect()
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Grass(Tile):
	def __init__(self, x, y):
		super(Grass, self).__init__(self, x, y)
		self.image = GRASS
		main_screen.blit(self.image, (self.rect.x, self.rect.y))

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('I am a Window')
		self.display = pygame.display.set_mode((WIDTH, HEIGHT))

	def draw_grid(self):
		for X in range(0, WIDTH, TILESIZE):
			pygame.draw.line(main_screen, (255, 0, 0), (X, 0), (X, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(main_screen, (255, 0, 0), (0, y), (WIDTH, y))

	def create_wall(self, x, y):
		list_of_walls.append(Wall(main_screen, x, y))

	def create_grass(self, x, y):
		list_of_grass.append(Grass(x, y))

def read_map():
	map_to_list = []
	with open(map, 'r') as file:
		for line in file:
			map_to_list.append(line.strip())

	for row, tiles in enumerate(map_to_list):
		for col, tile in enumerate(tiles):
			if tile == 'w':
				Game.create_wall(main_screen, col, row)
			if tile == 'G':
				Game.create_grass(main_screen, col,row)

play_game = True
main_screen = Game().display
player = Player(main_screen, 4, 4)

pygame.key.set_repeat(100, 50)

while play_game:
	Game.draw_grid(main_screen)
	read_map()
	player.event()
	player.spawn()

	pygame.display.flip()
	main_screen.fill((0, 0, 0))
	clock.tick(30)

