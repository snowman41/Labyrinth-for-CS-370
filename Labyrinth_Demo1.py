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
#CS370
#Labyrinth Demo

from Labyrinth_Demo1_Functions import *
import settings
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


BLACK = (0,0,0)#Colors used in game
GRAY = (120,120,120)
BACKGROUNDCOLOR = (0, 48, 146)

numOfColumns = 7
numOfRows = 7

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



os.chdir("C:\LabyrinthDemo")#Grabs image files from directory
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

randomizeTiles()#randomizes tiles

while not gameOver:
	for event in pygame.event.get():#Empties event queue
		if event.type == pygame.QUIT:#Sent when User presses close button
			gameOver = True

	screen.fill(BACKGROUNDCOLOR)

	for row in range(numOfRows):#Draws the grid		
		for column in range(numOfColumns):			
			pygame.draw.rect(screen, BLACK, [(gridMargin + singleGridWidth) * column + gridMargin + 250, (gridMargin + singleGridHeight) * row + gridMargin + 110, singleGridWidth, singleGridHeight])  

	if players >= 1: #player setup if statement, place to initialize player objects
		player_one = Player_Class.Player_Guy(p1, screen)
		player_one.place_player(screen)
		players -= 1

	mouse = pygame.mouse.get_pos()#initialize mouse pointer
	#click = pygame.mouse.get_pressed()#initialize mouse clicker	


	placeTiles()#Places all tiles
	

	mouse = pygame.mouse.get_pos()#initialize mouse pointer
	#click = pygame.mouse.get_pressed()#initialize mouse clicker
	
	screen.blit(getImage("LabyrinthTile1.png"), (255, 115))#Placing fixed tiles
	screen.blit(getImage("LabyrinthTile7.png"), (885, 115))
	screen.blit(getImage("LabyrinthTile43.png"), (255, 745))
	screen.blit(getImage("LabyrinthTile49.png"), (885, 745))

	left = pygame.draw.rect(screen, GRAY,(1000,650,75,50))#Create Buttons For Movement and Handle mouse clicks
	if 1000+75 > mouse[0] > 1000 and 650+50 > mouse[1] > 650:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("left")
				dirr = 0
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	down = pygame.draw.polygon(screen, GRAY, ((1115, 610), (1115, 635), (1105, 635), (1130, 660), (1155, 635), (1145, 635), (1145, 610)))
	if 1105+50 > mouse[0] > 1105 and 610+50 > mouse[1] > 610:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("down")
				dirr = 1
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	up = pygame.draw.polygon(screen, GRAY, ((1130, 520), (1105, 545), (1115, 545), (1115, 570), (1145, 570), (1145, 545), (1155, 545)))
	if 1105+50 > mouse[0] > 1105 and 520+50 > mouse[1] > 520:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("up")
				dirr = 2
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	right = pygame.draw.polygon(screen, GRAY, ((1150, 575), (1150, 605), (1175, 605), (1175, 615), (1200, 590), (1175, 565), (1175, 575)))
	if 1150+50 > mouse[0] > 1150 and 565+50 > mouse[1] > 565:#while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("right")
				dirr = 3
				player_one.move_player(dirr)#call move_player function on player and pass direction
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	
	
	player_one.place_player(screen)#keep player updated on screen




	pygame.draw.polygon(screen, (0, 0, 0), ((140, 245), (140, 295), (190, 295), (190, 320), (240, 270), (190, 220), (190, 245))) #Row 2, Moving Left. Pos 1
	if 140+100 > mouse[0] > 140 and 220+100 > mouse[1] > 220: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 1")
				pos = 1
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((140, 455), (140, 505), (190, 505), (190, 530), (240, 480), (190, 430), (190, 455))) #Row 4, Moving Left. Pos 2
	if 140+100 > mouse[0] > 140 and 430+100 > mouse[1] > 430: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 2")
				pos = 2
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((140, 665), (140, 715), (190, 715), (190, 740), (240, 690), (190, 640), (190, 665))) #Row 6, Moving Left. Pos 3
	if 140+100 > mouse[0] > 140 and 640+100 > mouse[1] > 640: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 3")
				pos = 3
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	
	pygame.draw.polygon(screen, (0, 0, 0), ((385, 0), (385, 50), (360, 50), (410, 100), (460, 50), (435, 50), (435, 0))) #Column 2, Moving Down. Pos 4
	if 360+100 > mouse[0] > 360 and 0+100 > mouse[1] > 0: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 4")
				pos = 4
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	
	pygame.draw.polygon(screen, (0, 0, 0), ((595, 0), (595, 50), (570, 50), (620, 100), (670, 50), (645, 50), (645, 0))) #Column 4, Moving Down. Pos 5
	if 570+100 > mouse[0] > 570 and 0+100 > mouse[1] > 0: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 5")
				pos = 5
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	
	pygame.draw.polygon(screen, (0, 0, 0), ((805, 0), (805, 50), (780, 50), (830, 100), (880, 50), (855, 50), (855, 0))) #Column 6, Moving Down. Pos 6
	if 780+100 > mouse[0] > 780 and 0+100 > mouse[1] > 0: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 6")
				pos = 6
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((1100, 245), (1050, 245), (1050, 220), (1000, 270), (1050, 320), (1050, 295), (1100, 295))) #Row 2, Moving Right. Pos 7
	if 1000+100 > mouse[0] > 1000 and 220+100 > mouse[1] > 220: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 7")
				pos = 7
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((1100, 455), (1050, 455), (1050, 430), (1000, 480), (1050, 530), (1050, 505), (1100, 505))) #Row 4, Moving Right. Pos 8
	if 1000+100 > mouse[0] > 1000 and 430+100 > mouse[1] > 430: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 8")
				pos = 8
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((1100, 665), (1050, 665), (1050, 640), (1000, 690), (1050, 740), (1050, 715), (1100, 715))) #Row 6, Moving Right. Pos 9
	if 1000+100 > mouse[0] > 1000 and 640+100 > mouse[1] > 640: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 9")
				pos = 9
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((385, 960), (385, 910), (360, 910), (410, 860), (460, 910), (435, 910), (435, 960))) #Column 2, Moving Up. Pos 10
	if 360+100 > mouse[0] > 360 and 860+100 > mouse[1] > 860: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 10")
				pos = 10
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((595, 960), (595, 910), (570, 910), (620, 860), (670, 910), (645, 910), (645, 960))) #Column 4, Moving Up. Pos 11
	if 570+100 > mouse[0] > 570 and 860+100 > mouse[1] > 860: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 11")
				pos = 11
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0

	pygame.draw.polygon(screen, (0, 0, 0), ((805, 960), (805, 910), (780, 910), (830, 860), (880, 910), (855, 910), (855, 960))) #Column 6, Moving Up. Pos 12
	if 780+100 > mouse[0] > 780 and 860+100 > mouse[1] > 860: #while mouse is within button perimitter
			if event.type == pygame.MOUSEBUTTONUP and prog == 0:#when mouse button is released
				print("Tile inserted at pos 12")
				pos = 12
				#Call function to move tile
				prog = 1
			if event.type == pygame.MOUSEBUTTONDOWN and prog == 1:
				prog = 0
	
	player_one.place_player(screen)#keep player updated on screen
	
  
	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library
