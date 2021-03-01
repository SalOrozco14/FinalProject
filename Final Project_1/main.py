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
"""
import pygame
from pygame.locals import *

pygame.init()

#set screen sizes - Sal
screen_width = 800
screen_height = 500

#create screen - Sal
screen = pygame.display.set_mode((screen_width, screen_height))

#Game Caption - Sal
pygame.display.set_caption('Space Rescue')

#Game LOOP - Sal
KeepGoing = True
while KeepGoing:

    for event in pygame.event.get():
        #closes window when 'X' is clicked
        if event.type == pygame.QUIT:
            KeepGoing = False

pygame.quit()
