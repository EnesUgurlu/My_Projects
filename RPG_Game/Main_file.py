import sys
from pygame.locals import *
from RPG_Game.Variables import *
from RPG_Game.Tiles import *


class Camera:
	def __init__(self, width, height):
		self.camera = pygame.Rect(0, 0, width, height)
		self.width = width
		self.height = height

	def apply(self, entity):
		return entity.rect.move(self.camera.topleft)

	def update(self, target):
		x = -target.rect.x + int(WIDTH / 2)
		y = -target.rect.y + int(HEIGHT / 2)
		self.camera = pygame.Rect(x, y, self.width, self.height)


class Game:
	def __init__(self):
		pygame.init()
		self.display = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('I am a Window')
		self.player = Player(self.display, 4, 4)
		pygame.key.set_repeat(100, 50)

	def draw_grid(self):
		for X in range(0, WIDTH, TILESIZE):
			pygame.draw.line(Game().display, (211,211,211), (X, 0), (X, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(Game().display, (211,211,211), (0, y), (WIDTH, y))

	def run_game(self):
		play_game = True

		while play_game:
			self.draw_grid()
			self.player.event()
			self.player.spawn()
			pygame.display.flip()

			clock.tick(30)

	def read_map(self):
		map_to_list = []
		with open(map, 'r') as mapfile:
			for mapline in mapfile:
				map_to_list.append(mapline.strip())

		for row, tiles in enumerate(map_to_list):
			for col, tile in enumerate(tiles):
				if tile == 'w':
					# Wall(col, row)
					# list_of_walls.append(wall)
					# self.display.blit(wall.image, (wall.rect.x, wall.rect.y))
					pass
				if tile == 'G':
					self.create_grass(col, row)

	# def create_wall(self, x, y):
	# 	wall = Wall(x, y)


	def create_grass(self, x, y):
		grass = Grass(x, y)
		list_of_grass.append(grass)
		self.display.blit(grass.image, (grass.rect.x, grass.rect.y))

	def new(self):
		self.draw_grid()
		self.camera = Camera(map_width, map_height)

	def apply_cam(self):
		self.display.blit(self.player.image, self.camera.apply(self.player))

	def update_cam(self):
		self.camera.update(self.player)

class Player:
	def __init__(self, game, x, y):
		self.game = game
		self.x = x * TILESIZE
		self.y = y * TILESIZE
		self.image = PLAYER
		self.rect = self.image.get_rect()

	def spawn(self):
		Game().display.blit(PLAYER, (self.x, self.y))

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



game = Game()

while True:
	game.new()
	game.run_game()

