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

os.chdir("C:\LabyrinthDemo")#Grabs image files from directory
for file in glob.glob("*.png"):
    imagePaths.append(file)



#Player_1 = Player_Class()

pygame.init()#initializes pygame
WINDOW_SIZE = [1280, 960]
screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen
pygame.display.set_caption("Labyrinth")#Sets title of the screen
gameOver = False#Loops until user closes out of game
clock = pygame.time.Clock()#Manages how fast the screen updates



#getTileCoordinates(12)#Gets coordinates for selected tile

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

	
	
	player_one.place_player(screen)#keep player updated on screen
	
	clock.tick(60)#Sets to 60 frames per second

	pygame.display.flip()

pygame.quit()#deactivates the pygame library