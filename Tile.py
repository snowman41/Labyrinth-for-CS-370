import sys
import os


class Tile:#create class for tiles characteristics
	def __init__(self, north, east, south, west, row, column):
		self.north = north#A property to indicate whether the tile is open on a given side, 0 = closed, 1 = open
		self.east = east
		self.south = south
		self.west = west
		#A property to store whether the tile has a treasure, when we implement separate treasures we can have this store the specific treasure name/number
		self.p1 = 0#Stores whether player1 is on the tile, we can add additional properties when we start dealing with multiple players
		self.currentrow = row
		self.currentcolumn = column
		self.image = ""
	def get_image_filepath(self):#Takes Tile class instance
		if self.North == 1:
			FilenameNorth = "North"
		else:
			FienameNorth = ""
		if self.East == 1:
			FilenameEast = "East"
		else:
			FilenameEast = ""
		if self.South == 1:
			FilenameSouth = "South"
		else:
			FilenameSouth = ""
		if self.West == 1:
			FilenameWest = "West"
		else:
			FilenameWest = ""
		self.image = ("%%%%.png" (FilenameNorth, FilenameEast, FilenameSouth, FilenameWest))#Make sure this matches the naming convention for tiles
		
