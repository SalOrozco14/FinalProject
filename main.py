"""
Sprite
---------
Enemy - sal = alien - sal =ufo - paige = boss?

player - PAIGE

rockship - Paige 

weapon? lazer change colors - PAIGE

item: life pick up (red moon rock), weapon (yellow/blue moon rock) - find temp

environment- platform? = pixal floor- temp

backgroung img - PAIGE

sounds: lazer, background music, blasting sound, boss sound when hit, item pick up =  Sal


intro page - Sal
==========
explain story - saving his friend
instructions
start button


player UML - paige
===============
var 
===
-life
+weapon grade

method
=======
setWeapon
setHealth
getWeapon
getHealth
Jump
shoot
walk
sound



Enemy UML - sal
=============
var
===
+Health

method
========
+StillAlive
walk
jump
sound



Boss UML *Extend from Enemy - sal
========
var
==
+Health -OVERRIDER
+weapon

method
=======
StillAlive
walk 
jump 
shoot
sound


Documentation
================
https://docs.google.com/document/d/1dKxxUuqAPKO6HxcVrZH8hl6K6uM-d8vUfVP5f6Ou9FU/edit?usp=sharing

"""
import pygame

#import world data
import World_1
#import player class
import Player

#import enemy class
#import Enemy 

pygame.init()

#set screen sizes and create screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


#create player object and image. Also rezises player image, and position it inside the screen
playerImg = pygame.image.load('Cat.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
Player1 = Player.Player(0,519)


#background image, and resize image to match screen size
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))


#Game Caption 
pygame.display.set_caption('Space Rescue')

#Set tile size for game. Will be used to setup floor, item, and enemy positions
tile_size = 50


#function draws grid on screen
#NOT PART OF THE GAME. HELP TO LAYOUT THE PLATFORM
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

#WORLD AND LEVEL CREATION
#*******************************************		
#CREATE LEVEL ONE
Level_1 =[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#call world to create levels
world = World_1.World_1(Level_1,tile_size, screen)
#*******************************************

#Game LOOP 
KeepGoing = True
while KeepGoing:

    #DRAW SECTION
    #==========================================
    #display background
    screen.blit(background, (0,0))
    
    #Draws the grid---NOT PART OF THE GAME
    draw_grid()

    #Draw tile on screen
    world.draw()
    
    #==========================================
    
    for event in pygame.event.get():
        #closes window when 'X' is clicked
        if event.type == pygame.QUIT:
            KeepGoing = False

          #if keystroke is pressed check whether its right or left 
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            Player1.Player_Left()
        if event.key == pygame.K_RIGHT:
            Player1.Player_Right()

            """"
        if event.key == pygame.K_UP:
            Player1.Player_Jump()

            """
            
    #set player on screen
    screen.blit(playerImg,(Player1.get_PlayerX(),Player1.get_PlayerY()))

    pygame.display.update()
pygame.quit()
