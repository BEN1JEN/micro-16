import pygame as pg
from font import get_letter

import screen

def get_button(button):
	keys = pygame.key.get_pressed()
	if button == "_A" or button == 0:
		return keys[pg.K_z]
	if button == "_B" or button == 1:
		return keys[pg.K_x]
	if button == "_U" or button == 2:
		return keys[pg.K_up]
	if button == "_D" or button == 3:
		return keys[pg.K_down]
	if button == "_L" or button == 4:
		return keys[pg.K_left]
	if button == "_R" or button == 5:
		return keys[pg.K_right]

def display_print(text, x, y, inv=False):
	x = int(x)
	y = int(y)
	for i, c in enumerate(text):
		letter = get_letter(c)
		for ly, row in enumerate(letter):
			for lx, pixel in enumerate(row):
				tx = x+lx+(i*4)
				ty = y+ly
				if inv:
					pixel = not pixel
				screen.set_pixel(tx, ty, pixel)
