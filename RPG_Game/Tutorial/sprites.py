import pygame
from Tutorial.settings import *

vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = game.player_img
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def get_keys(self, dx=0, dy=0):
		dx, dy = 0, 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.move(dx=-1)
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.move(dx=1)
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.move(dy=-1)
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.move(dy=1)

	def move(self, dx=0, dy=0):
		if not self.collide_with_walls(dx, dy):
			self.x += dx
			self.y += dy


	def collide_with_walls(self, dx=0, dy=0):
		for wall in self.game.walls:
			if wall.x == self.x + dx and wall.y == self.y + dy:
				return True
		return False

	def update(self):
		self.get_keys()
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE





