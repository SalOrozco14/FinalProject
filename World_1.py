""" Will be used to collect level data and generate world outline """
import pygame


class World_1():
    def __init__(self, data, size, gameScreen):

        self.tile_list = []
        self.tile_size = size

        self.screen = gameScreen
        #get attributes of the screen object
        self.screenInfo = pygame.display.Info()

        self.screen_h = self.screenInfo.current_h
        self.screen_w = self.screenInfo.current_w

        #Game Caption
        pygame.display.set_caption('Space Rescue')

        #load images
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(
            self.background, (self.screen_w, self.screen_h))

        img_1 = pygame.image.load('images/Rock.png')
        img_2 = pygame.image.load('images/newlaser.png')

        #runs through level matrix
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(
                        img_1, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img2 = pygame.transform.scale(
                        img_2, (self.tile_size, self.tile_size))
                    img_rect = img2.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img2, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

#Function adds tiles to the screen

    def draw(self):
        #display background
        self.screen.blit(self.background, (0, 0))

        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            #temp draw rectangle
            #pygame.draw.rect(self.screen,(255,255,255),tile[1],2)
