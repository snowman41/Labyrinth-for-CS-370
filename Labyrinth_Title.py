import pygame 
import sys
import os
import Input_Text_Box
from enum import Enum
from pygame.rect import Rect
from Sprite import *
from Labyrinth_Main import main_game
from Labyrinth_Client import establish_connection



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
			game_state = main_game(screen)

		if game_state == GameState.RULES:
			game_state = rules_screen(screen)

		if game_state == GameState.CONNECT:
			game_state = connect_screen(screen)

		if game_state == GameState.CONNECT_to_server:
			game_state = establish_connection(ip_text_box.Fetch_string, port_text_box.Fetch_string)

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
		center_position=(640, 725),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text= "Quit",
		action= GameState.QUIT,
	)
    
	#Create Quit Game Button
	connect_btn = UIElement(
		center_position=(640, 650),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text= "Connect",
		action= GameState.CONNECT,
	)

	buttons = [start_btn, quit_btn, rules_btn, connect_btn]

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

		#Set background color
		screen.fill(BLACK)

		rules_image = pygame.image.load(r'Rules.png')
		screen.blit(rules_image, (196, 115))

		mouse_up = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				mouse_up = True
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
		if ui_action is not None:
			return ui_action
		return_btn.draw(screen)

		#Set to 60 FPS
		clock.tick(60)
		pygame.display.flip()
        
        
def connect_screen(screen):
	ip_text_box = Input_Text_Box.input_text_box(screen, 500, 500, 300, 30, WHITE)
	port_text_box = Input_Text_Box.input_text_box(screen, 500, 450, 300, 30, WHITE)

	while True:

		#Create Return Button
		return_btn = UIElement(
		center_position=(640, 725),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="Return to Main Menu",
		action= GameState.TITLE,
		)

		connect_info = UIElement(
		center_position=(640, 400),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="Please Enter server IP address and Port:",
		action= GameState.TITLE,
		)

		IP_info = UIElement(
		center_position=(450, 450),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="IP:",
		action= GameState.TITLE,
		)

		PORT_info = UIElement(
		center_position=(430, 510),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text="PORT:",
		action= GameState.TITLE,
		)
        
		IP_string = UIElement(
		center_position=(650, 515),
		font_size=30,
		bg_rgb= WHITE,
		text_rgb= BLACK,
		text= ip_text_box.Fetch_string(),
		action= GameState.TITLE,
		)
        
		PORT_string = UIElement(
		center_position=(650, 465),
		font_size=30,
		bg_rgb= WHITE,
		text_rgb= BLACK,
		text= port_text_box.Fetch_string(),
		action= GameState.TITLE,
		)
        
		connect_server = UIElement(
		center_position=(650, 650),
		font_size=30,
		bg_rgb= BLACK,
		text_rgb= WHITE,
		text= "[Connect to Server]",
		action= establish_connection(ip_text_box.Fetch_string, port_text_box.Fetch_string()),
		)


		#Set background color
		screen.fill(BLACK)

		mouse_up = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				mouse_up = True
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		ip_text_box.Update()
		port_text_box.Update()





		ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
		if ui_action is not None:
			return ui_action
		ui_action_two = connect_server.update(pygame.mouse.get_pos(), mouse_up)
		if ui_action_two is not None:
			return ui_action_two
		return_btn.draw(screen)
		connect_info.draw(screen)
		IP_info.draw(screen)
		PORT_info.draw(screen)
		IP_string.draw(screen)
		PORT_string.draw(screen)
		connect_server.draw(screen)
		#Set to 60 FPS
		clock.tick(60)
		pygame.display.flip()


#Enumerated States
class GameState(Enum) :
	QUIT = -1
	TITLE = 0
	GAME = 1
	RULES = 2
	CONNECT = 3
	CONNECT_to_server = 4

if __name__ == "__main__":
	main()