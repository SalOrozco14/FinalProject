"""
********************************Space Platfrom Game***********************************

Main game program 
=================


Done
=====
screen created = Salvador 2/27/2021
Game loop created = Salvador 2/27/2021
Game exit event = Salvador 2/27/2021

still needs work
================
1
"""
import pygame
from Animate import Animate

#import world data
import World_1
#import player class
import Player

#import enemy class
#import Enemy

pygame.init()

#inter game clock and frame per sec setup
clock = pygame.time.Clock()
fps = 60

#set screen sizes and create screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Set tile size for game. Will be used to setup floor, item, and enemy positions
tile_size = 50

#create player object and image. Also rezises player image, and position it inside the screen
Player1R = Animate('playerImgs', 'R', 4, 'png', False, tile_size)
Player1L = Animate('playerImgs', 'R', 4, 'png', True, tile_size)

Player1RNew = Animate('playerImgs2', 'G', 4, 'png', False, tile_size)
Player1LNew = Animate('playerImgs2', 'G', 4, 'png', True, tile_size)

Player1 = Player.Player(screen, Player1R, Player1L, 0, 450)
#load player image files for animation
"""
#function draws grid on screen
#NOT PART OF THE GAME. HELP TO LAYOUT THE PLATFORM
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
"""
#WORLD AND LEVEL CREATION
#*******************************************
#CREATE LEVEL ONE
#CREATE LEVEL ONE
Level_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#call world to create levels
world = World_1.World_1(Level_1, tile_size, screen)
#*******************************************

#GAME LOOP CONTROL AND JUMPING CONDITIONAL
KeepGoing = True
jumped = False
PlayerRect = Player1.rect

#GAME LOOP
#*******************************************************@
while KeepGoing:
    #set frame per sec inside game loop
    clock.tick(fps)

    #DRAW SECTION
    #==============================================

    #Draw tile on screen
    world.draw()

    #Draws the grid---NOT PART OF THE GAME
    #draw_grid()

    #=============================================

    for event in pygame.event.get():
        #closes window/game
        if event.type == pygame.QUIT:
            KeepGoing = False

            #GAME CONTROLS
    #=============================================
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and jumped == False:
        Player1.Player_Jump()
        jumped = True
    if key[pygame.K_SPACE] == False:
        jumped = False
        Player1.Player_Gravity()

    if key[pygame.K_LEFT]:
        Player1.Player_Left()
    if key[pygame.K_RIGHT]:
        Player1.Player_Right()
    #=============================================

    #Check for collision between player and game blocks
    #need to get tile list from world_1 class to do collision checks
    for tile in world.tile_list:
        #check for collision in the Y direction
        if tile[1].colliderect(Player1.rect):
            #print("collision")
            #check if below the ground
            if Player1.rect.bottom > tile[1].top:
                #print("tile top: "+str(tile[1].top))
                #print("Player rect Y: "+str(Player1.rect.y))
                Player1.rect.y = tile[1].top - 50
                #print("Bottom player collision")

            elif Player1.rect.top <= tile[1].bottom:
                #print("TOP player collision")
                Player1.jump = 0
                Player1.rect.top += 50

                #print("tile bottom: "+str(tile[1].bottom))
                #print("Player rect Y: "+str(Player1.rect.y))

            #check if above the ground

            #if Player1.jump >= 0:
            #   Player1.rect.y = tile[1].top - Player1.rect.bottom
            #  print("Top player collision")

    #Draw player on screen and updates player coordinates
    Player1.draw()

    pygame.display.update()
pygame.quit()
#*******************************************************@
