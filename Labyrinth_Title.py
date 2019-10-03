import pygame 
import sys
import os
from pygame.rect import Rect
from Sprite import *

#Colors used in game
WHITE = (255,255,255)
GRAY = (120,120,120)
BLACK = (0, 0, 0)

pygame.init()

#Screen dimensions
width = 1280
height = 960

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labyrinth")

clock = pygame.time.Clock()
gameover = False
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

#Create Quit Game Button
quit_btn = UIElement(
	center_position=(640, 600),
	font_size=30,
	bg_rgb= BLACK,
	text_rgb= WHITE,
	text="Quit",
	#action = sys.exit(),
)

#Create Start Game Button
start_btn = UIElement(
	center_position=(640, 500),
	font_size=30,
	bg_rgb= BLACK,
	text_rgb= WHITE,
	text="Start Game",
	#action= (bring player to game screen),
)


buttons = [start_btn, quit_btn]

#Main game loop
while True:
	
	mouse_up = False
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			mouse_up = True
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#Set background color
	screen.fill(BLACK)

	#Set and display Logo
	logo = pygame.image.load(r'Main_Logo.png')
	screen.blit(logo, (118, 115))


	#Draw and update buttons
	for button in buttons:
		button.draw(screen)
		action = button.update(pygame.mouse.get_pos(), mouse_up)
		if action is not None:
			button.draw(screen)

	#Set to 60 FPS
	clock.tick(60)
	pygame.display.flip()