#CS370
#Labyrinth Demo

import pygame
import sys
import os

singleGridWidth = 100
singleGridHeight = 100
gridMargin = 5#Individual grid dimensions

BLACK = (0,0,0)#Colors used in game
BACKGROUNDCOLOR = (0, 48, 146)
#gridPosition = [100, 100]
#x = gridPosition[0]
#y = gridPosition[1]

numOfColumns = 7
numOfRows = 7

imageLibrary = {}#Defines dictionary

def getImage(path):#Function which takes in file path and initializes image
	global imageLibrary
	image = imageLibrary.get(path)
	if image == None:
		canonicalizedPath = path.replace("/", os.sep).replace("\\", os.sep)
		image = pygame.image.load(canonicalizedPath)
		imageLibrary[path] = image
	return image

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

pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates

while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			gameOver = True

	screen.fill(BACKGROUNDCOLOR)

	for row in range(numOfRows):#Draws the grid
		for column in range(numOfColumns):
			#surface = pygame.surface(100, 100)#Creates surface
			pygame.draw.rect(screen, BLACK, [(gridMargin + singleGridWidth) * column + gridMargin + 250, (gridMargin + singleGridHeight) * row + gridMargin + 110, singleGridWidth, singleGridHeight])  

	screen.blit(getImage("LabyrinthTile1.png"), (255, 115))#Placing fixed tiles
	screen.blit(getImage("LabyrinthTile7.png"), (885, 115))
	screen.blit(getImage("LabyrinthTile43.png"), (255, 745))
	screen.blit(getImage("LabyrinthTile49.png"), (885, 745))




	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library