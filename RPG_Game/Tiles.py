# from RPG_Game.Main_file import main_screen
from RPG_Game.Variables import *

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

class Wall(Tile):
	def __init__(self, x, y):
		super(Wall, self).__init__(self, x, y)
		self.image = WALL
