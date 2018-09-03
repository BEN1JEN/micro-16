import bpf
import screen
import engine

#bpf_init()
bpf.execute_command("print(hello there, ~test, twentynine())")

running = True
while running:
	delta, running = screen.update_pygame()
	#bpf_update(delta)
	#bpf_draw()
	screen.draw_display()

screen.quit()
