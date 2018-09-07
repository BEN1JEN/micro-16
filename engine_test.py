import engine
import screen

engine.set_output(draw_screen=True, draw_lcd=True)
engine.display_print("hello there", 16, 29)

running = True
while running:
	delta, running = screen.update_pygame()
	screen.draw_display()
