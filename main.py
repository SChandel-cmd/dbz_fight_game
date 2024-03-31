import pygame
from player import Player
from stage import Stage
from attack import Attack
from goku import Goku
from vegeta import Vegeta


pygame.init()
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("DBZ: BT 0")
pygame.mixer.init()
PLAYER_HEIGHT = 40
PLAYER_WIDTH = 15
FPS = 60

font_path = 'assets/fonts/PressStart2P-Regular.ttf' 
size = 28
my_font = pygame.font.Font(font_path, size)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# SCORE_FONT = pygame.font.SysFont("comicsans", 50)

background_ship = pygame.image.load('assets/images/background/ship.png')
background_ship = pygame.transform.scale(background_ship, (450, 250))
title = pygame.image.load('assets/images/menu/title-1.png')
title = pygame.transform.scale(title, (500, 50))
start_button = pygame.image.load('assets/images/menu/start.png')
start_button = pygame.transform.scale(start_button, (95, 50))
start_rect = start_button.get_rect()
start_rect.topleft = (WIDTH * 1 // 2.4, 150)
start_highlight_rect = pygame.Rect(WIDTH * 1 // 2.4 - 2, 150 - 2, 100, 55)
help_button = pygame.image.load('assets/images/menu/help.png')
help_button = pygame.transform.scale(help_button, (95, 50))
help_rect = help_button.get_rect()
help_rect.topleft = (WIDTH * 1 // 2.4, 220)
help_highlight_rect = pygame.Rect(WIDTH * 1 // 2.4 - 2, 220 - 2, 100, 55)
exit_button = pygame.image.load('assets/images/menu/exit.png')
exit_button = pygame.transform.scale(exit_button, (95, 50))
exit_rect = exit_button.get_rect()
exit_rect.topleft = (WIDTH * 1 // 2.4, 290)
exit_highlight_rect = pygame.Rect(WIDTH * 1 // 2.4 - 2, 290 - 2, 100, 55)
button_hover_sound = pygame.mixer.Sound("assets/sound_fx/button_hover.mp3")
button_hover_last = False
vegeta_wins = pygame.image.load('assets/images/menu/vegeta_wins.png')
goku_wins = pygame.image.load('assets/images/menu/goku_wins.png')
stock_3 = pygame.image.load('assets/images/menu/3.png')
stock_2 = pygame.image.load('assets/images/menu/2.png')
stock_1 = pygame.image.load('assets/images/menu/1.png')
pygame.mouse.set_cursor(*pygame.cursors.tri_left)


def color_calc(player):
	if 255 + 255 - player.dmg_taken <= 0:
		return (0, 0, 0)
	elif 255 - player.dmg_taken <= 0:
		return (255 + 255 - player.dmg_taken, 0, 0)
	else:
		return (255, 255 - player.dmg_taken, 255 - player.dmg_taken)


def draw_menu(win, time_val, mouse_pos, mouse_click, screen):
	global button_hover_last
	win.fill(BLACK)
	background_image = pygame.image.load('assets/images/background/px_' + str(int((time_val % 30) / 5)) + '.png')
	background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
	win.blit(background_image, (0, 0))
	win.blit(background_ship, (130, 260))
	# x_font = my_font.render('test123', True, WHITE)
	# win.blit(x_font, (30, 40))
	if time_val < 120:
		win.blit(title, (100, time_val - 90))
	else:
		win.blit(title, (100, 30))
	if start_rect.collidepoint(mouse_pos):
		if not button_hover_last:
			button_hover_sound.play()
		button_hover_last = True
		if mouse_click:
			screen[0] = 1
		pygame.draw.rect(win, (0, 0, 0), start_highlight_rect)
	elif help_rect.collidepoint(mouse_pos):
		if not button_hover_last:
			button_hover_sound.play()
		button_hover_last = True
		pygame.draw.rect(win, (0, 0, 0), help_highlight_rect)
	elif exit_rect.collidepoint(mouse_pos):
		if not button_hover_last:
			button_hover_sound.play()
		button_hover_last = True
		pygame.draw.rect(win, (0, 0, 0), exit_highlight_rect)
		if mouse_click:
			exit()
	else:
		button_hover_last = False
	win.blit(start_button, (WIDTH * 1 // 2.4, 150))
	win.blit(help_button, (WIDTH * 1 // 2.4, 220))
	win.blit(exit_button, (WIDTH * 1 // 2.4, 290))
	pygame.display.update()


def draw_game(win, left_player, right_player, stage, attacks, time_val):
	win.fill(BLACK)
	# left_stock_text = SCORE_FONT.render(f"{left_player.stocks}", 1, WHITE)
	# right_stock_text = SCORE_FONT.render(f"{right_player.stocks}", 1, WHITE)
	# left_dmg_text = SCORE_FONT.render(f"{left_player.dmg_taken}", 1, WHITE)
	# right_dmg_text = SCORE_FONT.render(f"{right_player.dmg_taken}", 1, WHITE)
	left_color = color_calc(left_player)
	right_color = color_calc(right_player)
	background_image = pygame.image.load('assets/images/background/px_' + str(int((time_val % 30) / 5)) + '.png')
	background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
	win.blit(background_image, (0, 0))
	win.blit(background_ship, (130, 260))
	pygame.draw.circle(win, BLACK, (WIDTH // 6 + 10, 40), 40)  # (x, y) coordinates of the center, radius
	pygame.draw.circle(win, BLACK, (WIDTH * 5 // 6, 40), 40)  # (x, y) coordinates of the center, radius

	# pygame.draw.circle(win, RED, (466, 263), 1)  # 1 pixel radius for a point
	# win.blit(left_stock_text, (WIDTH//4 - left_stock_text.get_width()//2, 20))
	# win.blit(right_stock_text, (WIDTH*3//4 - right_stock_text.get_width()//2, 20))
	# win.blit(left_dmg_text, (WIDTH//4 - left_dmg_text.get_width()//2, 40))
	# win.blit(right_dmg_text, (WIDTH*3//4 - right_dmg_text.get_width()//2, 40))
	# left_player.draw(win)
	# right_player.draw(win)
	Goku().draw(win, left_player, attacks[0])
	Vegeta().draw(win, right_player, attacks[1])
	circle_surface_1 = pygame.Surface((200, 200), pygame.SRCALPHA)
	circle_surface_2 = pygame.Surface((200, 200), pygame.SRCALPHA)

	# pygame.draw.circle(circle_surface_1, left_color, (WIDTH // 6 + 10, 40), 40)
	# pygame.draw.circle(circle_surface_2, right_color, (WIDTH * 5 // 6, 40), 40)
	# win.blit(circle_surface_1, (0, 0))
	# win.blit(circle_surface_2, (0, 0))
	left_dmg = my_font.render(str(left_player.dmg_taken)+'%', True, left_color)
	right_dmg = my_font.render(str(right_player.dmg_taken)+ '%', True, right_color)
	win.blit(left_dmg, (60, 60))
	win.blit(right_dmg, (510, 60))
	# win.blit(x_font, (30, 40))
	if left_player.stocks == 3:
		win.blit(stock_3, (150, 60))
	elif left_player.stocks == 2:
		win.blit(stock_2, (150, 60))
	else:
		win.blit(stock_1, (150, 60))
	if right_player.stocks == 3:
		win.blit(stock_3, (600, 60))
	elif right_player.stocks == 2:
		win.blit(stock_2, (600, 60))
	else:
		win.blit(stock_1, (600, 60))
	# for attack in attacks:
	# 	attack.draw(win)
	# stage.draw(win)
	pygame.display.update()


def main():
	screen = [0]
	run = True
	clock = pygame.time.Clock()
	fight_music_file = "assets/music/fight_music.mp3"
	menu_music_file = "assets/music/menu_music.mp3"
	victory_music_file = "assets/music/victory_music.mp3"
	left_player = Player(WIDTH * 2 // 5, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH * 2, PLAYER_HEIGHT * 2, 2.5,
						 pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_f, pygame.K_g, pygame.K_v,
						 False)
	right_player = Player(WIDTH * 3 // 5, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH * 2, PLAYER_HEIGHT * 2, 2.5,
						  pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_j, pygame.K_k, pygame.K_m,
						  True)
	stage = Stage(WIDTH // 3 - 35, HEIGHT // 2 + 50, WIDTH // 2 - 30, HEIGHT // 4)
	left_attack = Attack(left_player)
	right_attack = Attack(right_player)
	time_val = 0
	screen_0_switch = True
	screen_1_switch = True
	mouse_click = False
	while run:
		time_val += 1
		clock.tick(FPS)
		# print(clock)
		if screen[0] == 0:
			mouse_pos = pygame.mouse.get_pos()
			if screen_0_switch:
				pygame.mixer.music.load(menu_music_file)
				pygame.mixer.music.play(loops=-1)
				pygame.mixer.music.set_volume(0.3)
				screen_0_switch = False
				screen_1_switch = True
			draw_menu(WIN, time_val, mouse_pos, mouse_click, screen)

		if screen[0] == 1:
			if screen_1_switch:
				pygame.mixer.music.load(fight_music_file)
				pygame.mixer.music.play(loops=-1)
				pygame.mixer.music.set_volume(0.3)
				screen_1_switch = False
				screen_0_switch = True
			draw_game(WIN, left_player, right_player, stage, [left_attack, right_attack], time_val)
			keys = pygame.key.get_pressed()
			left_player.handle_movement(keys)
			right_player.handle_movement(keys)
			left_player.handle_attack(keys, left_attack)
			right_player.handle_attack(keys, right_attack)
			left_attack.update(right_player)
			right_attack.update(left_player)
			stage.activate_y_gravity(left_player)
			stage.activate_y_gravity(right_player)
			stage.activate_x_gravity(left_player)
			stage.activate_x_gravity(right_player)
			stage.handle_sliding(left_player)
			stage.handle_sliding(right_player)
			stage.handle_out_of_bounds(left_player)
			stage.handle_out_of_bounds(right_player)
			left_player.handle_getting_hit(right_attack, right_player)
			right_player.handle_getting_hit(left_attack, left_player)
			left_player.update_cooldown()
			right_player.update_cooldown()

			won = False
			if right_player.stocks == 0:
				won = True
				WIN.blit(goku_wins,
						 (WIDTH // 2 - goku_wins.get_width() // 2, HEIGHT // 2 - goku_wins.get_height() // 2))

			if left_player.stocks == 0:
				won = True
				WIN.blit(vegeta_wins,
						 (WIDTH // 2 - vegeta_wins.get_width() // 2, HEIGHT // 2 - vegeta_wins.get_height() // 2))
			if won:
				pygame.mixer.music.load(victory_music_file)
				pygame.mixer.music.play()
				pygame.display.update()
				pygame.time.delay(5000)
				left_player.reset()
				left_player.reset_stocks()
				right_player.reset()
				right_player.reset_stocks()
				screen = [0]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_click = True
			elif event.type == pygame.MOUSEBUTTONUP:
				mouse_click = False

	pygame.quit()


if __name__ == '__main__':
	main()
