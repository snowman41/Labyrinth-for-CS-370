import pygame 
import sys
import os
from enum import Enum
from pygame.rect import Rect
from Sprite import *


#Global Colors used
WHITE = (255,255,255)
GRAY = (120,120,120)
BLACK = (0, 0, 0)

#Init clock
clock = pygame.time.Clock()

#Main function to track gamestate
def main():
	pygame.init()

	#Init GameState to title
	game_state = GameState.TITLE

	#Screen dimensions
	width = 1280
	height = 960

	#Set Screen dimensions and caption
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Labyrinth")

	#Begin music loop
	pygame.mixer.music.load('background.mp3')
	pygame.mixer.music.play(-1)

	#Gamestate switch
	while True:
		if game_state == GameState.TITLE:
			game_state = title_screen(screen)

		if game_state == GameState.GAME:
			#game_state = play_game(screen)
			#Quit game for now until we connect the pieces
			pygame.quit()

		if game_state == GameState.RULES:
			game_state = rules_screen(screen)

		if game_state == GameState.QUIT:
			pygame.quit()
			sys.exit()
			return

#Main function of Title Screen
def title_screen(screen):

	#Create Rules Button
	rules_btn = UIElement(
		center_position=(640, 500),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="Rules of the Game",
		action= GameState.RULES,
	)

	#Create Start Game Button
	start_btn = UIElement(
		center_position=(640, 575),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text= "Start Game",
		action= GameState.GAME,
	)

	#Create Quit Game Button
	quit_btn = UIElement(
		center_position=(640, 650),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text= "Quit",
		action= GameState.QUIT,
	)

	buttons = [start_btn, quit_btn, rules_btn]

	#Main Title Screen Loop
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
			#button.draw(screen)
			ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
			if ui_action is not None:
				return ui_action
			button.draw(screen)

		#Set to 60 FPS
		clock.tick(60)
		pygame.display.flip()


#Main function of Rules Screen
def rules_screen(screen):

	while True:

		#Create Return Button
		return_btn = UIElement(
		center_position=(640, 575),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="Return to Main Menu",
		action= GameState.TITLE,
		)

		mouse_up = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				mouse_up = True
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Set background color
		screen.fill(BLACK)

		ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
		if ui_action is not None:
			return ui_action
		return_btn.draw(screen)

		#Set to 60 FPS
		clock.tick(60)
		pygame.display.flip()


#Enumerated States
class GameState(Enum) :
	QUIT = -1
	TITLE = 0
	GAME = 1
	RULES = 2

if __name__ == "__main__":
	main()