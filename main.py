import pygame as pg
import bpf

# variables:
screen_size = [1280, 640]
screen = []
for x in range(128):
	screen.append([])
	for y in range(64):
		screen[x].append(True)

# initalyze pygame
pg.init()
pg.display.init()
surface = pg.display.set_mode(screen_size, pg.RESIZABLE)
clock = pg.time.Clock()

# draw_display function
def draw_display():
	for x, column in enumerate(screen):
		for y, pixel in enumerate(column):
			if pixel:
				pg.draw.rect(surface, [255, 255, 255], [x*10, y*10, 10, 10])
	pg.display.flip()


#bpf_init()

while True:
	delta = clock.tick(30)
	#bpf_update(delta)
	#bpf_draw()
	draw_display()
