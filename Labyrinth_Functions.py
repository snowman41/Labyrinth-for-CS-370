#Functions

import pygame
import sys
import os
import random
import numpy 
from random import shuffle
import glob
from Tile import *

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

def get_tile_coordinates(row, col):#Function which takes in column and row and returns coordinates of tile
	colRow = tuple([row, col])#Stores col row as coordinate value

	for c in range(7):
		for r in range(7):
			coords = tuple([r*100+(100*3), c*100+100])#Stores coordinate value for current row and column
			pos = tuple([r, c])
			if pos == colRow:
				#print(coords)
				return(coords)

def grab_and_place_arrows(display):#Function which grabs images of arrows and puts them in positions around board
	mouse = pygame.mouse.get_pos()#Stores position of mouse	

	arrowDownIC = pygame.image.load("ArrowDownIC.png")
	arrowDownAC = pygame.image.load("ArrowDownAC.png")
	arrowUPIC = pygame.image.load("ArrowUPIC.png")
	arrowUPAC = pygame.image.load("ArrowUPAC.png")
	arrowLeftIC = pygame.image.load("ArrowLeftIC.png")
	arrowLeftAC = pygame.image.load("ArrowLeftAC.png")
	arrowRightIC = pygame.image.load("ArrowRightIC.png")
	arrowRightAC = pygame.image.load("ArrowRightAC.png")


	if 400 + 100 > mouse[0] > 400 and 0 + 100 > mouse[1] > 20:#If mouse hovers, then changes image
		display.blit(arrowDownAC, (435, 70))
	else:
		display.blit(arrowDownIC, (435, 35))

	if 600 + 100 > mouse[0] > 600 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (635, 70))
	else:
		display.blit(arrowDownIC, (635, 35))

	if 800 + 100 > mouse[0] > 800 and 0 + 100 > mouse[1] > 20:
		display.blit(arrowDownAC, (835, 70))
	else:
		display.blit(arrowDownIC, (835, 35))

	if 400 + 100 > mouse[0] > 400 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (435, 800))
	else:
		display.blit(arrowUPIC, (435, 835))

	if 600 + 100 > mouse[0] > 600 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (635, 800))
	else:
		display.blit(arrowUPIC, (635, 835))

	if 800 + 100 > mouse[0] > 800 and 780 + 100 > mouse[1] > 800:
		display.blit(arrowUPAC, (835, 800))
	else:
		display.blit(arrowUPIC, (835, 835))

	if 200 + 100 > mouse[0] > 220 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowRightAC, (273, 235))
	else:
		display.blit(arrowRightIC, (238, 235))

	if 200 + 100 > mouse[0] > 220 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowRightAC, (273, 435))
	else:
		display.blit(arrowRightIC, (238, 435))

	if 200 + 100 > mouse[0] > 220 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowRightAC, (273, 635))
	else:
		display.blit(arrowRightIC, (238, 635))

	if 980 + 100 > mouse[0] > 1000 and 200 + 100 > mouse[1] > 200:
		display.blit(arrowLeftAC, (998, 235))
	else:
		display.blit(arrowLeftIC, (1033, 235))

	if 980 + 100 > mouse[0] > 1000 and 400 + 100 > mouse[1] > 400:
		display.blit(arrowLeftAC, (998, 435))
	else:
		display.blit(arrowLeftIC, (1033, 435))

	if 980 + 100 > mouse[0] > 1000 and 600 + 100 > mouse[1] > 600:
		display.blit(arrowLeftAC, (998, 635))
	else:
		display.blit(arrowLeftIC, (1033, 635))

def grab_and_place_movement_keys(display):#Function which grabs images of movement keys and places them in correct positions
	mouse = pygame.mouse.get_pos()#Stores position of mouse	
	click = pygame.mouse.get_pressed()

	moveUpIC = pygame.image.load("moveUpIC.png")
	moveRightIC = pygame.image.load("moveRightIC.png")
	moveDownIC = pygame.image.load("moveDownIC.png")
	moveLeftIC = pygame.image.load("moveLeftIC.png")
	moveUpAC = pygame.image.load("moveUpAC.png")
	moveRightAC = pygame.image.load("moveRightAC.png")
	moveDownAC = pygame.image.load("moveDownAC.png")
	moveLeftAC = pygame.image.load("moveLeftAC.png")	

	if 1110 + 45 > mouse[0] > 1125 and 800 + 60 > mouse[1] > 800:#If mouse clicks, then changes image
		display.blit(moveUpIC, (1110, 800))
		if click[0] == 1:
			display.blit(moveUpAC, (1110, 800))
	else:
		display.blit(moveUpIC, (1110, 800))

	if 1110 + 45 > mouse[0] > 1125 and 870 + 60 > mouse[1] > 870:
		display.blit(moveDownIC, (1110, 870))
		if click[0] == 1:
			display.blit(moveDownAC, (1110, 870))
	else:
		display.blit(moveDownIC, (1110, 870))

	if 1160 + 45 > mouse[0] > 1160 and 825 + 60 > mouse[1] > 845:
		display.blit(moveRightIC, (1160, 835))
		if click[0] == 1:
			display.blit(moveRightAC, (1160, 835))
	else:
		display.blit(moveRightIC, (1160, 835))

	if 1060 + 45 > mouse[0] > 1060 and 825 + 60 > mouse[1] > 845:
		display.blit(moveLeftIC, (1060, 835))
		if click[0] == 1:
			display.blit(moveLeftAC, (1060, 835))
	else:
		display.blit(moveLeftIC, (1060, 835))



def grab_and_randomize_tiles():#Function which grabs tiles in specified directory and puts them in random positions in matrix
	elbowTiles = []#Stores elbow tiles
	straightTiles = []#Stores straight tiles 
	tTiles = []#Stores T Tiles
	randomImagePaths = []#Stores random rotated image paths

	#elbowFiles = ("NorthEast*", "NorthWest*", "*EastSouth*", "SouthWest*")
	#straightFiles = ("NorthSouth*", "EastWest*")
	#TFiles = ("NorthEastSouth*", "NorthEastWest*", "NorthSouthWest*", "EastSouthWest*")

	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in random positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory

	#for files in elbowFiles:
		#elbowTiles.extend(glob.glob(files))
	#for files in straightFiles:
		#straightTiles.extend(glob.glob(files))
	#for files in TFiles:
		#tTiles.extend(glob.glob(files))
	for file in glob.glob("NorthEast.png"):
		elbowTiles.append(file)
	for file in glob.glob("NorthWest*"):
		elbowTiles.append(file)
	for file in glob.glob("EastSouth.png"):
		elbowTiles.append(file)
	for file in glob.glob("SouthWest*"):
		elbowTiles.append(file)
	for file in glob.glob("NorthSouth.png"):
		straightTiles.append(file)
	for file in glob.glob("EastWest*"):
		straightTiles.append(file)
	for file in glob.glob("NorthEastSouth*"):
		tTiles.append(file)
	for file in glob.glob("NorthEastWest*"):
		tTiles.append(file)
	for file in glob.glob("NorthSouthWest*"):
		tTiles.append(file)
	for file in glob.glob("EastSouthWest*"):
		tTiles.append(file)
	for x in range(15):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(elbowTiles))
	for x in range(13):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(straightTiles)) 
	for x in range(6):#Number of unfixed elbow tiles
		randomImagePaths.append(random.choice(tTiles))

	for r in range(7):
		for c in range(7):
			currPos = tuple([r, c])
			if currPos == (0, 1) or currPos == (0, 3) or currPos == (0, 5) or currPos == (1, 0) or currPos == (1, 1) or currPos == (1, 2) or currPos == (1, 3) or currPos == (1, 4) or currPos == (1, 5) or currPos == (1, 6) or currPos == (2, 1) or currPos == (2, 3) or currPos == (2, 5) or currPos == (3, 0) or currPos == (3, 1) or currPos == (3, 2) or currPos == (3, 3) or currPos == (3, 4) or currPos == (3, 5) or currPos == (3, 6) or currPos == (4, 1) or currPos == (4, 3) or currPos == (4, 5) or currPos == (5, 0) or currPos == (5, 1) or currPos == (5, 2) or currPos == (5, 3) or currPos == (5, 4) or currPos == (5, 5) or currPos == (5, 6) or currPos == (6, 1) or currPos == (6, 3) or currPos == (6, 5):#checks if current position is for non fixed tiles
				imagePath = random.choice(randomImagePaths)
				twoDimBoard[r][c] = imagePath
				randomImagePaths.remove(imagePath)

	return twoDimBoard

def grab_fixed_tiles():#Function which grabs tiles in specified directory and puts them in fixed positions in matrix
	twoDimBoard = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles in fixed positions

	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory

	for file in glob.glob("Starting*"):
		twoDimBoard[0][0] = file#Matrix goes by row first and column second
	for file in glob.glob("SouthWest*"):
		twoDimBoard[6][0] = file
	for file in glob.glob("NorthWest*"):
		twoDimBoard[6][6] = file
	for file in glob.glob("NorthEast.png"):
		twoDimBoard[0][6] = file
	for file in glob.glob("EastSouthWest*"):
		twoDimBoard[2][0] = file
		twoDimBoard[4][0] = file
		twoDimBoard[4][2] = file
	for file in glob.glob("NorthEastSouth*"):
		twoDimBoard[0][2] = file
		twoDimBoard[2][2] = file
		twoDimBoard[0][4] = file
	for file in glob.glob("NorthSouthWest*"):
		twoDimBoard[6][2] = file
		twoDimBoard[4][4] = file
		twoDimBoard[6][4] = file
	for file in glob.glob("NorthEastWest*"):
		twoDimBoard[2][4] = file
		twoDimBoard[2][6] = file
		twoDimBoard[4][6] = file

	return twoDimBoard


def get_image_filepath(tile):#Takes Tile class instance
	STARTING01 = pygame.image.load(os.path.join('..\LabyrinthProject', 'Starting01.png')).convert_alpha()#Gets the image path for tile
	NORTHEAST = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEast.png')).convert_alpha()
	NORTHWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthWest.png')).convert_alpha()
	EASTSOUTH = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastSouth.png')).convert_alpha()
	SOUTHWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'SouthWest.png')).convert_alpha()
	NORTHSOUTH = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthSouth.png')).convert_alpha()
	EASTWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastWest.png')).convert_alpha()
	NORTHEASTSOUTH = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEastSouth.png')).convert_alpha()
	NORTHEASTWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthEastWest.png')).convert_alpha()
	NORTHSOUTHWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'NorthSouthWest.png')).convert_alpha()
	EASTSOUTHWEST = pygame.image.load(os.path.join('..\LabyrinthProject', 'EastSouthWest.png')).convert_alpha()

	tile.image = ("%%%%.png" (tile.North, tile.East, tile.South, tile.West))#Make sure this matches the naming convention for tiles

def rotate_tile_clockwise(tile):
	tilevalue = tile.north
	tile.north = tile.west
	tile.west = tile.south
	tile.south = tile.east
	tile.east = tilevalue

def new_tile_initialization():
	#TILE_ARRAY = allFilePaths
	#TILE_ARRAY = [[0 for x in range(7)] for x in range(7)]#Creates matrix to store tiles
	#get_tile_coordinates(0, 0),STARTING01,
	TILE_ARRAY = numpy.ndarray(shape=(7,7), dtype=object)
	t0 = Tile(0,1,1,0)#initialize and place all of the tiles that dont move
	TILE_ARRAY[0][0]=t0
	t1 = Tile(0,1,1,1)
	TILE_ARRAY[2][0]=t1
	t2 = Tile(0,1,1,1)
	TILE_ARRAY[4][0]=t2
	t3 = Tile(0,0,1,1)
	TILE_ARRAY[6][0]=t3
	t4 = Tile(1,1,1,0)
	TILE_ARRAY[0][2]=t4
	t5 = Tile(1,1,1,0)
	TILE_ARRAY[2][2]=t5
	t6 = Tile(0,1,1,1)
	TILE_ARRAY[4][2]=t6
	t7 = Tile(1,0,1,1)
	TILE_ARRAY[6][2]=t7
	t8 = Tile(1,1,1,0)
	TILE_ARRAY[0][4]=t8
	t9 = Tile(1,1,0,1)
	TILE_ARRAY[2][4]=t9
	t10 = Tile(1,0,1,1)
	TILE_ARRAY[4][4]=t10
	t11 = Tile(1,0,1,1)
	TILE_ARRAY[6][4]=t11
	t12 = Tile(1,1,0,0)
	TILE_ARRAY[0][6]=t12
	t13 = Tile(1,1,0,1)
	TILE_ARRAY[2][6]=t13
	t14 = Tile(1,1,0,1)
	TILE_ARRAY[4][6]=t14
	t15 = Tile(1,0,0,1)
	TILE_ARRAY[6][6]=t15
	t16 = Tile(1,0,1,0)#Straight tiles
	t17 = Tile(1,0,1,0)
	t18 = Tile(1,0,1,0)
	t19 = Tile(1,0,1,0)
	t20 = Tile(1,0,1,0)
	t21 = Tile(1,0,1,0)
	t22 = Tile(1,0,1,0)
	t23 = Tile(1,0,1,0)
	t24 = Tile(1,0,1,0)
	t25 = Tile(1,0,1,0)
	t26 = Tile(1,0,1,0)
	t27 = Tile(1,0,1,0)
	t28 = Tile(1,0,1,0)
	t29 = Tile(1,1,0,0)#Elbow tiles
	t30 = Tile(1,1,0,0)
	t31 = Tile(1,1,0,0)
	t32 = Tile(1,1,0,0)
	t33 = Tile(1,1,0,0)
	t34 = Tile(1,1,0,0)
	t35 = Tile(1,1,0,0)
	t36 = Tile(1,1,0,0)
	t37 = Tile(1,1,0,0)
	t38 = Tile(1,1,0,0)
	t39 = Tile(1,1,0,0)
	t40 = Tile(1,1,0,0)
	t41 = Tile(1,1,0,0)
	t42 = Tile(1,1,0,0)
	t43 = Tile(1,1,0,0)
	t44 = Tile(1,1,1,0)#T tiles
	t45 = Tile(1,1,1,0)
	t46 = Tile(1,1,1,0)
	t47 = Tile(1,1,1,0)
	t48 = Tile(1,1,1,0)
	t49 = Tile(1,1,1,0)#extra tile

	initializationList = [t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49]

	for a in initializationList:
		for b in range(random.randint(0,3)):
			rotate_tile_clockwise(a)
	random.shuffle(initializationList)
	for column in range(7):
		for row in range(7):
			#if [row][column] != t0 or [row][column] != t1 or [row][column] != t2 or [row][column] != t3 or [row][column] != t4 or [row][column] != t5 or [row][column] != t6 or [row][column] != t7 or [row][column] != t8 or [row][column] != t9 or [row][column] != t10 or [row][column] != t11 or [row][column] != t12 or [row][column] != t13 or [row][column] != t14 or [row][column] != t15:
			if TILE_ARRAY[row][column] == None:#This is testing if TILE_ARRAY[row][column] is empty, may have to change logic to work
				TILE_ARRAY[row][column] = initializationList[0]
				del initializationList[0]

	print(TILE_ARRAY)#shows contents of tile_array
	return TILE_ARRAY