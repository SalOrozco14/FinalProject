""" Will be used to collect level data and generate world outline """
import pygame

class World_1():
    
	def __init__(self, data, size , gameScreen):
		self.tile_list = []
		self.tile_size = size
		self.screen = gameScreen
		#load images
		rock_img = pygame.image.load('Rock.png')

		#runs through level matrix
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(rock_img, (self.tile_size, self.tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * self.tile_size
					img_rect.y = row_count * self.tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	#Function adds tiles to the screen
	def draw(self):
		for tile in self.tile_list:
			self.screen.blit(tile[0], tile[1])

	    
