#Functions

import settings

import pygame
import sys
import os
from random import shuffle
import glob

settings.init()#initializes global variables
imageLibrary = {}

def getImage(path):#Function which takes in file path and initializes image
	global imageLibrary
	image = imageLibrary.get(path)
	if image == None:
		canonicalizedPath = path.replace("/", os.sep).replace("\\", os.sep)
		image = pygame.image.load(canonicalizedPath)
		imageLibrary[path] = image
	return image

def getTileCoordinates(tileNum):#Function which gives coordinates of tile
	listOfCoords = []#Stores coordinates
	index = 0
	xVal = 255
	yVal = 115

	for x in range(49):#Fill ListOfCoords with coordinates
		if(x < 7):		
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 14):
			if (x == 7):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 21):
			if (x == 14):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 28):
			if (x == 21):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 35):
			if (x == 28):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 42):
			if (x == 35):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
		elif(x < 49):
			if (x == 42):
				xVal = 255
				yVal += 105
			coords = tuple([xVal , yVal])
			listOfCoords.insert(x ,coords)
			xVal += 105
	for coords in listOfCoords:
		if(tileNum - 1 == index):			
			return coords
		index += 1
			
def filterTilePaths(path):#Filters through the fixed tiles
	if '01' in path or '03' in path or '05' in path or '07' in path or '15' in path or '17' in path or '19' in path or '21' in path or '29' in path or '31' in path or '33' in path or '35' in path or '43' in path or '45' in path or '47' in path or '49' in path or 'PlayerOne' in path:
		return True
	else:
		return False
def randomizeTiles():#Randomizes tiles that are not fixed 
	os.chdir("..\LabyrinthDemo")#Grabs image files that are from directory
	for file in glob.glob("*.png"):
		settings.imagePaths.append(file)

	filteredPaths=filter(filterTilePaths, settings.imagePaths)#Grabs fixed tiles

	for tileImage in filteredPaths:#Removes fixed tiles from list
		settings.imagePaths.remove(tileImage)

	for startingTile in settings.imagePaths:#For some reason previous for loop doesn't get rid of starting tile, so this does
		if startingTile == 'LabyrinthTile01.png':
			settings.imagePaths.remove(startingTile)

	shuffle(settings.imagePaths)#Shuffles the order of the image paths

def placeTiles():#Places tiles onto grid
	settings.screen.blit(getImage(settings.imagePaths[0]), (getTileCoordinates(2)))#Placing random tiles
	settings.screen.blit(getImage(settings.imagePaths[1]), (getTileCoordinates(4)))
	settings.screen.blit(getImage(settings.imagePaths[2]), (getTileCoordinates(6)))
	settings.screen.blit(getImage(settings.imagePaths[3]), (getTileCoordinates(8)))
	settings.screen.blit(getImage(settings.imagePaths[4]), (getTileCoordinates(9)))
	settings.screen.blit(getImage(settings.imagePaths[5]), (getTileCoordinates(10)))
	settings.screen.blit(getImage(settings.imagePaths[6]), (getTileCoordinates(11)))
	settings.screen.blit(getImage(settings.imagePaths[7]), (getTileCoordinates(12)))
	settings.screen.blit(getImage(settings.imagePaths[8]), (getTileCoordinates(13)))
	settings.screen.blit(getImage(settings.imagePaths[9]), (getTileCoordinates(14)))
	settings.screen.blit(getImage(settings.imagePaths[10]), (getTileCoordinates(16)))
	settings.screen.blit(getImage(settings.imagePaths[11]), (getTileCoordinates(18)))
	settings.screen.blit(getImage(settings.imagePaths[12]), (getTileCoordinates(20)))
	settings.screen.blit(getImage(settings.imagePaths[13]), (getTileCoordinates(22)))
	settings.screen.blit(getImage(settings.imagePaths[14]), (getTileCoordinates(23)))
	settings.screen.blit(getImage(settings.imagePaths[15]), (getTileCoordinates(24)))
	settings.screen.blit(getImage(settings.imagePaths[16]), (getTileCoordinates(25)))
	settings.screen.blit(getImage(settings.imagePaths[17]), (getTileCoordinates(26)))
	settings.screen.blit(getImage(settings.imagePaths[18]), (getTileCoordinates(27)))
	settings.screen.blit(getImage(settings.imagePaths[19]), (getTileCoordinates(28)))
	settings.screen.blit(getImage(settings.imagePaths[20]), (getTileCoordinates(30)))
	settings.screen.blit(getImage(settings.imagePaths[21]), (getTileCoordinates(32)))
	settings.screen.blit(getImage(settings.imagePaths[22]), (getTileCoordinates(34)))
	settings.screen.blit(getImage(settings.imagePaths[23]), (getTileCoordinates(36)))
	settings.screen.blit(getImage(settings.imagePaths[24]), (getTileCoordinates(37)))
	settings.screen.blit(getImage(settings.imagePaths[25]), (getTileCoordinates(38)))
	settings.screen.blit(getImage(settings.imagePaths[26]), (getTileCoordinates(39)))
	settings.screen.blit(getImage(settings.imagePaths[27]), (getTileCoordinates(40)))
	settings.screen.blit(getImage(settings.imagePaths[28]), (getTileCoordinates(41)))
	settings.screen.blit(getImage(settings.imagePaths[29]), (getTileCoordinates(42)))
	settings.screen.blit(getImage(settings.imagePaths[30]), (getTileCoordinates(44)))
	settings.screen.blit(getImage(settings.imagePaths[31]), (getTileCoordinates(46)))
	settings.screen.blit(getImage(settings.imagePaths[32]), (getTileCoordinates(48)))

	settings.screen.blit(getImage("LabyrinthTile01.png"), (getTileCoordinates(1)))#Placing fixed tiles
	settings.screen.blit(getImage("LabyrinthTile03.png"), (getTileCoordinates(3)))
	settings.screen.blit(getImage("LabyrinthTile05.png"), (getTileCoordinates(5)))
	settings.screen.blit(getImage("LabyrinthTile07.png"), (getTileCoordinates(7)))
	settings.screen.blit(getImage("LabyrinthTile15.png"), (getTileCoordinates(15)))
	settings.screen.blit(getImage("LabyrinthTile17.png"), (getTileCoordinates(17)))
	settings.screen.blit(getImage("LabyrinthTile19.png"), (getTileCoordinates(19)))
	settings.screen.blit(getImage("LabyrinthTile21.png"), (getTileCoordinates(21)))
	settings.screen.blit(getImage("LabyrinthTile29.png"), (getTileCoordinates(29)))
	settings.screen.blit(getImage("LabyrinthTile31.png"), (getTileCoordinates(31)))
	settings.screen.blit(getImage("LabyrinthTile33.png"), (getTileCoordinates(33)))
	settings.screen.blit(getImage("LabyrinthTile35.png"), (getTileCoordinates(35)))
	settings.screen.blit(getImage("LabyrinthTile43.png"), (getTileCoordinates(43)))
	settings.screen.blit(getImage("LabyrinthTile45.png"), (getTileCoordinates(45)))
	settings.screen.blit(getImage("LabyrinthTile47.png"), (getTileCoordinates(47)))
	settings.screen.blit(getImage("LabyrinthTile49.png"), (getTileCoordinates(49)))