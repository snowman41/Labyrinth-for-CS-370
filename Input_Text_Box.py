import pygame 
import sys
import os
from enum import Enum
from pygame.rect import Rect
from Sprite import *
from Labyrinth_Main import main_game

class input_text_box():
    def __init__(self, screen, x_pos, y_pos, width, hieght, color):
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.hieght = hieght
        self.color = color
        self.string = ""
        
    def Update(self):
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, self.color, (self.x_pos, self.y_pos, self.width, self.hieght))
        if self.x_pos + self.width > mouse[0] > self.x_pos and self.y_pos + self.hieght > mouse[1] > self.y_pos:#If mouse hovers, then changes image
            pygame.time.delay(100)
            if pygame.key.get_pressed()[pygame.K_0] == 1:
                self.string += "0"
            if pygame.key.get_pressed()[pygame.K_1] == 1:
                self.string += "1"
            if pygame.key.get_pressed()[pygame.K_2] == 1:
                self.string += "2"
            if pygame.key.get_pressed()[pygame.K_3] == 1:
                self.string += "3"
            if pygame.key.get_pressed()[pygame.K_4] == 1:
                self.string += "4"
            if pygame.key.get_pressed()[pygame.K_5] == 1:
                self.string += "5"
            if pygame.key.get_pressed()[pygame.K_6] == 1:
                self.string += "6"
            if pygame.key.get_pressed()[pygame.K_7] == 1:
                self.string += "7"
            if pygame.key.get_pressed()[pygame.K_8] == 1:
                self.string += "8"
            if pygame.key.get_pressed()[pygame.K_9] == 1:
                self.string += "9"
            if pygame.key.get_pressed()[pygame.K_BACKSPACE] == 1:
                self.string = self.string[:-1]
            if pygame.key.get_pressed()[pygame.K_PERIOD] == 1:
                self.string += "."
        else:
            pygame.draw.rect(self.screen, 10, (self.x_pos+2, self.y_pos+10, self.width*.10, self.hieght*.10))
        
    def Fetch_string(self):
        stringer = self.string
        return stringer