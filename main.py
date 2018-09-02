import pygame as pg
import bpf

# variables:
screen_size = [1280, 640]
screen = []
for x in range(128):
	screen.append([])
	for y in range(64):
		screen[x].append(False)

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
bpf.execute_command(screen, "print(hello there, 16, 29)")

running = True
while running:
	for event in pg.event.get(): # User did something
		if event.type == pg.QUIT: # If user clicked close
			running=False # Flag that we are done so we exit this loop
	delta = clock.tick(30)
	#bpf_update(delta)
	#bpf_draw()
	draw_display()

pg.quit()
