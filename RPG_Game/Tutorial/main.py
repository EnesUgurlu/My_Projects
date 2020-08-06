import pygame
import sys
from os import path
from Tutorial.settings import *
from Tutorial.sprites import *
from Tutorial.tilemap import *


class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		pygame.key.set_repeat(500, 100) # This repeat function allows continuous movement without a loop
		self.load_data()


	def load_data(self):
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, 'images')
		self.map = Map(path.join(game_folder, 'map2.txt'))
		self.player_img = pygame.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

	def new(self):
		# Initialize all variables and do all the setup for a new game
		self.all_sprites = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()

		for row, tiles in enumerate(self.map.data):
			for col, tile in enumerate(tiles):
				if tile == '1':
					Wall(self, col, row)
				if tile == 'P':
					self.player = Player(self, col, row)

		self.camera = Camera(self.map.width, self.map.height)

	def run(self):
		# Game loop - set self.playing to False to end the game
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS) / 1000
			self.player.update()
			self.events()
			self.update()
			self.draw()

	def quit(self):
		pygame.quit()
		sys.exit()

	def update(self):
		# Update portion of game loop
		self.all_sprites.update()
		self.camera.update(self.player)

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))


	def draw(self):
		self.screen.fill(BGCOLOUR)
		self.draw_grid()
		for sprite in self.all_sprites:
			self.screen.blit(sprite.image, self.camera.apply(sprite))

		pygame.display.flip()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()

	def show_start_screen(self):
		pass

	def show_go_screen(self):
		pass



game = Game()
game.show_start_screen()

while True:
	game.new()
	game.run()
	game.show_go_screen()







