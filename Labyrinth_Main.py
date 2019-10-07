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
PURPLE = (108, 16, 212)
LIGHT_PURPLE = (172, 98, 255)
GREEN = (0, 255, 0)
BACKGROUNDCOLOR = (0, 48, 146)

ROW_COUNT = 7
COLUMN_COUNT = 7
SQUARESIZE = 100

randomTilePositions = grab_and_randomize_tiles()#Stores positions of all un-fixed tiles in 7x7 matrix
fixedTilePositions = grab_fixed_tiles()#Stores positions of all fixed tiles in 7x7 matrix

while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			sys.exit()

	screen.fill(BACKGROUNDCOLOR)

	for c in range(ROW_COUNT):#creates gameboard
		for r in range(COLUMN_COUNT):
			pygame.draw.rect(screen, BLACK, (c*SQUARESIZE+(SQUARESIZE*3), r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

	button(screen, "SHUFFLE!", GREEN, "GristledFont-Regular.ttf", 35, 50, 850, 150, 75, PURPLE, LIGHT_PURPLE)#Creates shuffle button

	for c in range(ROW_COUNT):#Fills game board with random and fixed tiles
		for r in range(COLUMN_COUNT):
			if randomTilePositions[c][r] != 0:
				randomTile = pygame.image.load(randomTilePositions[c][r])
				screen.blit(randomTile, (get_tile_coordinates(c, r)))
			elif randomTilePositions[c][r] == 0:
				fixedTile = pygame.image.load(fixedTilePositions[c][r])
				screen.blit(fixedTile, (get_tile_coordinates(c, r)))



	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library