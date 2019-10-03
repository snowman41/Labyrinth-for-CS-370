#Functions

import pygame
import sys
import os
from random import shuffle
import glob
import numpy as np

def get_tile_coordinates(col, row):#Function which returns coordinates of tile
	listOfCoords = []
	currPosition = []

	colRow = tuple([col, row])

	for c in range(7):
		for r in range(7):
			coords = tuple([c*100+(100*3), r*100+100])#Stores coordinate value for current row and column
			pos = tuple([c, r])
			if pos == colRow:
				return(coords)


#def grab_and_randomize_images():
#	originalImagePaths = []#stores image names from desired directory
#	elbowTiles = []#stores elbow tiles
#	straightTiles = []#stores straight tiles 
#	TTiles = []#stores T Tiles

#	os.chdir("..\LabyrinthProject")#Grabs image files that are from directory
#	for file in glob.glob("Elbow*"):
#		elbowTiles.append
#	print(elbowTiles)
		



