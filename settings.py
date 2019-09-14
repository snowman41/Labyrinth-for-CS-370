#Contains global variables

import pygame

def init():
	global imagePaths
	imagePaths = []
	global WINDOW_SIZE
	WINDOW_SIZE = [1280, 960]
	global screen
	screen = pygame.display.set_mode(WINDOW_SIZE)#Sets the size of the screen