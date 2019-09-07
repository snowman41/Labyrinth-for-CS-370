#Functions

import pygame
import sys
import os
import glob

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
			print(coords)
			return coords
		index += 1
			




