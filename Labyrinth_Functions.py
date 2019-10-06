#Functions

import pygame
import sys
import os
import random
from random import shuffle
import glob
import numpy as np

def button(display, txt, txtColor, font, fontSize, x, y, w, h, ic, ac):#Function which creates button, (display: source of screen) (txt: what the button says) (txtColor: Color of text) (font: what font the text will be) (x, y: coordinates of button) (w, h: width and height of button) (ic, ac: inactive and active color)
	mouse = pygame.mouse.get_pos()#Stores position of mouse
	#click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(display, ac, (x, y, w, h))
	else:
		pygame.draw.rect(display, ic, (x, y, w, h))

	smallText = pygame.font.Font(font, fontSize)
	textSurf, textRect = text_objects(txt, smallText, txtColor)
	textRect.center = ((x + (w / 2)), (y + (h/2)))
	display.blit(textSurf, textRect)

def text_objects(text, font, color):#Defines text contents, font and color for text
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def get_tile_coordinates(col, row):#Function which takes in column and row and returns coordinates of tile
	colRow = tuple([col, row])#Stores col row as coordinate value

	for c in range(7):
		for r in range(7):
			coords = tuple([c*100+(100*3), r*100+100])#Stores coordinate value for current row and column
			pos = tuple([c, r])
			if pos == colRow:
				return(coords)


def grab_and_randomize_tiles():#Function which grabs tiles in specified directory and puts them in random positions in matrix
	elbowTiles = []#Stores elbow tiles
	straightTiles = []#Stores straight tiles 
	tTiles = []#Stores T Tiles
	randomImagePaths = []#Stores random rotated image paths

	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in random positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory
	for file in glob.glob("Elbow*"):
		elbowTiles.append(file)
	for file in glob.glob("Straight*"):
		straightTiles.append(file)
	for file in glob.glob("T*"):
		tTiles.append(file)
	for x in range(15):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(elbowTiles))
	for x in range(13):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(straightTiles)) 
	for x in range(6):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(tTiles))

	for c in range(7):
		for r in range(7):
			currPos = tuple([c, r])
			if currPos == (0, 1) or currPos == (0, 3) or currPos == (0, 5) or currPos == (1, 0) or currPos == (1, 1) or currPos == (1, 2) or currPos == (1, 3) or currPos == (1, 4) or currPos == (1, 5) or currPos == (1, 6) or currPos == (2, 1) or currPos == (2, 3) or currPos == (2, 5) or currPos == (3, 0) or currPos == (3, 1) or currPos == (3, 2) or currPos == (3, 3) or currPos == (3, 4) or currPos == (3, 5) or currPos == (3, 6) or currPos == (4, 1) or currPos == (4, 3) or currPos == (4, 5) or currPos == (5, 0) or currPos == (5, 1) or currPos == (5, 2) or currPos == (5, 3) or currPos == (5, 4) or currPos == (5, 5) or currPos == (5, 6) or currPos == (6, 1) or currPos == (6, 3) or currPos == (6, 5):#checks if current position is for non fixed tiles
				imagePath = random.choice(randomImagePaths)
				twoDimBoard[c][r] = imagePath
				randomImagePaths.remove(imagePath)

	return twoDimBoard

def grab_fixed_tiles():#Function which grabs tiles in specified directory and puts them in fixed positions in matrix
	elbowTiles = []#Stores elbow tiles
	tTiles = []#Stores T Tiles

	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in fixed positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory
	for file in glob.glob("Starting*"):
		twoDimBoard[0][0] = file#Matrix goes by row first and column second
	for file in glob.glob("ElbowSouthWest*"):
		twoDimBoard[6][0] = file
	for file in glob.glob("ElbowWestNorth*"):
		twoDimBoard[6][6] = file
	for file in glob.glob("ElbowNorthEast*"):
		twoDimBoard[0][6] = file
	for file in glob.glob("TEastSouthWest*"):
		twoDimBoard[2][0] = file
		twoDimBoard[4][0] = file
		twoDimBoard[4][2] = file
	for file in glob.glob("TNorthEastSouth*"):
		twoDimBoard[0][2] = file
		twoDimBoard[2][2] = file
		twoDimBoard[0][4] = file
	for file in glob.glob("TNorthSouthWest*"):
		twoDimBoard[6][2] = file
		twoDimBoard[4][4] = file
		twoDimBoard[6][4] = file
	for file in glob.glob("TWestNorthEast*"):
		twoDimBoard[2][4] = file
		twoDimBoard[2][6] = file
		twoDimBoard[4][6] = file

	return twoDimBoard



		











		



