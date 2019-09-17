#CS370
#Labyrinth Demo

from Labyrinth_Demo1_Functions import *
import Player_Class
import pygame
import sys
import os
import random
#import Labyrinth_Demo1_Player_Class
import glob

singleGridWidth = 100
singleGridHeight = 100
gridMargin = 5#Individual grid dimensions
players = 1 #how many players
p1 = "marty"#player name
prog = 0#variable used to keep track of mouse clicks
#>>>>>>> Architectural-Spike

BLACK = (0,0,0)#Colors used in game
GRAY = (120,120,120)
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

class Tile:#create class for tiles characteristics
    def __init__(self, north, south, east, west, treasure):
        self.north = north#A property to indicate whether the tile is open on a given side, 0 = closed, 1 = open
        self.south = south
        self.east = east
        self.west = west
        self.treasure = treasure#A property to store whether the tile has a treasure, when we implement separate treasures we can have this store the specific treasure name/number
        self.p1 = 0#Stores whether player1 is on the tile, we can add additional properties when we start dealing with multiple players

Tile_Array = numpy.ndarray(shape=(7,7), dtype=object)#elements are accessed by 
t0 = Tile(0,1,1,0,0)#upper left corner tile
t1 = Tile(0,1,0,1,0)#upper right corner tile
t2 = Tile(1,0,1,0,0)#lower left corner tile
t3 = Tile(1,0,0,1,0)#lower right corner tile
Tile_Array[0,0]=t0
Tile_Array[0,6]=t1
Tile_Array[6,0]=t2
Tile_Array[6,6]=t3
print(Tile_Array)
print(Tile_Array[6,6].north)#Here you can access the contents of the tile by calling its location in the array!!!! Success!!!!
print(Tile_Array[6,6].south)
print(Tile_Array[6,6].east)
print(Tile_Array[6,6].west)
print(t3.north)
print(t3.south)
print(t3.east)
print(t3.west)

#<<<<<<< Architectural-Spike

os.chdir("..\LabyrinthDemo")#Grabs image files from directory
#=======
os.chdir("C:\LabyrinthDemo")#Grabs image files from directory
#>>>>>>> Architectural-Spike
for file in glob.glob("*.png"):
    imagePaths.append(file)
    print(file)
	

#getTileCoordinates(13)#Gets coordinates for selected tile

#<<<<<<< Architectural-Spike
#=======

#>>>>>>> Architectural-Spike
#Player_1 = Player_Class()

pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates

#<<<<<<< Architectural-Spike
#=======


#getTileCoordinates(12)#Gets coordinates for selected tile

#>>>>>>> Architectural-Spike
while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			gameOver = True

	screen.fill(BACKGROUNDCOLOR)

	for row in range(numOfRows):#Draws the grid		
		for column in range(numOfColumns):			
			pygame.draw.rect(screen, BLACK, [(gridMargin + singleGridWidth) * column + gridMargin + 250, (gridMargin + singleGridHeight) * row + gridMargin + 110, singleGridWidth, singleGridHeight])  
#<<<<<<< Architectural-Spike

#=======
#>>>>>>> Architectural-Spike
	if players >= 1: #player setup if statement, place to initialize player objects
		player_one = Player_Class.Player_Guy(p1, screen)
		player_one.place_player(screen)
		players -= 1
#<<<<<<< Architectural-Spike

	mouse = pygame.mouse.get_pos()#initialize mouse pointer
	#click = pygame.mouse.get_pressed()#initialize mouse clicker

	for x in range(49):#Filling board with tiles
		screen.blit(getImage(imagePaths[x]), (getTileCoordinates(x + 1)))	
#=======
#>>>>>>> Architectural-Spike

	mouse = pygame.mouse.get_pos()#initialize mouse pointer
	#click = pygame.mouse.get_pressed()#initialize mouse clicker
	
	screen.blit(getImage("LabyrinthTile1.png"), (255, 115))#Placing fixed tiles
	screen.blit(getImage("LabyrinthTile7.png"), (885, 115))
	screen.blit(getImage("LabyrinthTile43.png"), (255, 745))
	screen.blit(getImage("LabyrinthTile49.png"), (885, 745))
#<<<<<<< Architectural-Spike
	
#=======
#>>>>>>> Architectural-Spike
	left = pygame.draw.rect(screen, GRAY,(1000,650,75,50))#Create Buttons For Movement and Handle mouse clicks
	if 1000+75 > mouse[0] > 1000 and 650+50 > mouse[1] > 650:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("left")
				dirr = 0
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	down = pygame.draw.rect(screen, GRAY,(1100,650,75,50))
	if 1100+75 > mouse[0] > 1100 and 650+50 > mouse[1] > 650:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("down")
				dirr = 1
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	up = pygame.draw.rect(screen, GRAY,(1100,580,75,50))
	if 1100+75 > mouse[0] > 1100 and 580+50 > mouse[1] > 580:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("up")
				dirr = 2
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	right = pygame.draw.rect(screen, GRAY,(1200,650,75,50))
	if 1200+75 > mouse[0] > 1200 and 650+50 > mouse[1] > 650:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("right")
				dirr = 3
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
#<<<<<<< Architectural-Spike

	
	
	player_one.place_player(screen)#keep player updated on screen

#=======
#>>>>>>> Architectural-Spike

	
	
	player_one.place_player(screen)#keep player updated on screen
	
	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library
