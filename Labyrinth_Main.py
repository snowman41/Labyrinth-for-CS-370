#CS370
#Labyrinth


from Labyrinth_Functions import *
import pygame
import sys
import os
import glob
import random
import numpy as np

pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates

BLACK = (0,0,0)#Colors used in game
GRAY = (120,120,120)
BACKGROUNDCOLOR = (0, 48, 146)

ROW_COUNT = 7
COLUMN_COUNT = 7
SQUARESIZE = 100

grab_and_randomize_images()

get_tile_coordinates(3, 3)

while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			sys.exit()

	screen.fill(BACKGROUNDCOLOR)

	for c in range(ROW_COUNT):
		for r in range(COLUMN_COUNT):
			pygame.draw.rect(screen, BLACK, (c*SQUARESIZE+(SQUARESIZE*3), r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library