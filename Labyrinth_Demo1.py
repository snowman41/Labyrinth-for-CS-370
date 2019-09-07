#CS370
#Labyrinth Demo

from Labyrinth_Demo1_Functions import *
import pygame
import sys
import os
import random
import glob

singleGridWidth = 100
singleGridHeight = 100
gridMargin = 5#Individual grid dimensions

BLACK = (0,0,0)#Colors used in game
BACKGROUNDCOLOR = (0, 48, 146)

numOfColumns = 7
numOfRows = 7

imagePaths = []
imageLibrary = {}#Defines dictionary
alreadyUsedCoords = []#Stores already Used Coordinates

grid = []#Initializes list, used to populate grid
for row in range(numOfRows):
	grid.append([])#Adds empty array which will hold each cell
	for column in range(numOfColumns):
		grid[row].append(0)#Adds cell to list

currentRect = []#initializes list, used to hold individual rectangles(not being used currently)
for row in range(numOfRows):
	grid.append([])
	for column in range(numOfColumns):
		grid[row].append(0)

os.chdir("C:\pythonProjects\LabyrinthDemo")#Grabs image files from directory
for file in glob.glob("*.png"):
    imagePaths.append(file)





pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates



getTileCoordinates(13)#Gets coordinates for selected tile

while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			gameOver = True

	screen.fill(BACKGROUNDCOLOR)

	for row in range(numOfRows):#Draws the grid		
		for column in range(numOfColumns):			
			pygame.draw.rect(screen, BLACK, [(gridMargin + singleGridWidth) * column + gridMargin + 250, (gridMargin + singleGridHeight) * row + gridMargin + 110, singleGridWidth, singleGridHeight])  
			

	screen.blit(getImage("LabyrinthTile1.png"), (255, 115))#Placing fixed tiles
	screen.blit(getImage("LabyrinthTile7.png"), (885, 115))
	screen.blit(getImage("LabyrinthTile43.png"), (255, 745))
	screen.blit(getImage("LabyrinthTile49.png"), (885, 745))
	

	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library