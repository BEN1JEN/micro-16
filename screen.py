import pygame as pg

# initalyze pygame
pg.init()
clock = pg.time.Clock()
pg.display.init()

screen_size = [1280, 640]
surface = pg.display.set_mode(screen_size, pg.RESIZABLE)

screen = []
for x in range(128):
	screen.append([])
	for y in range(64):
		screen[x].append(False)

def set_pixel(x, y, p):
	screen[x][y] = not not p

def get_pixel(x, y):
	return screen[x][y]

def draw_display():
	for x, column in enumerate(screen):
		for y, pixel in enumerate(column):
			if pixel:
				pg.draw.rect(surface, [255, 255, 255], [x*10, y*10, 10, 10])
	pg.display.flip()

def update_pygame():
	running = True
	for event in pg.event.get(): # User did something
		if event.type == pg.QUIT: # If user clicked close
			running=False # Flag that we are done so we exit this loop
	return clock.tick(30), running

def quit():
	pg.quit()

def get_screen():
	return screen
