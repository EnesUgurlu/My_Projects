import sys
from pygame.locals import *
from RPG_Game.Variables import *
from RPG_Game.Tiles import *

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


class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('I am a Window')
		self.display = pygame.display.set_mode((WIDTH, HEIGHT))

	def draw_grid(self):
		for X in range(0, WIDTH, TILESIZE):
			pygame.draw.line(main_screen, (211,211,211), (X, 0), (X, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(main_screen, (211,211,211), (0, y), (WIDTH, y))

	def create_wall(self, x, y):
		wall = Wall(x, y)
		list_of_walls.append(wall)
		main_screen.blit(wall.image, (wall.rect.x, wall.rect.y))

	def create_grass(self, x, y):
		grass = Grass(x, y)
		list_of_grass.append(grass)
		main_screen.blit(grass.image, (grass.rect.x, grass.rect.y))

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
	read_map()
	Game.draw_grid(main_screen)
	player.event()
	player.spawn()

	pygame.display.flip()
	main_screen.fill((0, 0, 0))
	clock.tick(30)

