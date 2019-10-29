import sys
import os

class Tile:#create class for tiles characteristics
    def __init__(self, north, east, south, west):
        self.north = north#A property to indicate whether the tile is open on a given side, 0 = closed, 1 = open
        self.east = east
        self.south = south
        self.west = west
        self.treasure = treasure#A property to store whether the tile has a treasure, when we implement separate treasures we can have this store the specific treasure name/number
        self.p1 = 0#Stores whether player1 is on the tile, we can add additional properties when we start dealing with multiple players
