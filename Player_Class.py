from Labyrinth_Demo1_Functions import *
import pygame

class Player_Guy:#create class for player
    
    def __init__(self, name, screen):#initialize player with name and screen space
        print("Player instantiating")
        #getTileCoordinates(12)
        self.tile = 12 #set starting tile
        self.name = name
        self.screen = screen
        
        print("Player instantiated")
        print(self.tile)
        
    def place_player(self, screen):#places player on screen by objects current tile
        screen.blit(getImage("LabyrinthPlayerOneT.png"), getTileCoordinates(self.tile))

    def move_player(self, dirr):#take in direction from 0-3 and move player, left=0,down = 1, up = 2, right = 3
        if dirr == 0:
            self.tile = self.tile - 1
            self.screen.blit(getImage("LabyrinthPlayerOneT.png"), getTileCoordinates(self.tile))
        elif dirr == 1:
            self.tile = self.tile + 7
            self.screen.blit(getImage("LabyrinthPlayerOneT.png"), getTileCoordinates(self.tile))
        elif dirr == 2:
            self.tile = self.tile - 7
            self.screen.blit(getImage("LabyrinthPlayerOneT.png"), getTileCoordinates(self.tile))
        elif dirr == 3:
            self.tile = self.tile + 1
            self.screen.blit(getImage("LabyrinthPlayerOneT.png"), getTileCoordinates(self.tile))
