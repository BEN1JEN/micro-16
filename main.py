import bpf
import screen
import engine

#bpf_init()
bpf.execute_set_variable("test variable [ height ] = 16")
bpf.execute_command("print(hello there, 16, twentynine())")
bpf.execute_command("py_print(~table)")

running = True
while running:
	delta, running = screen.update_pygame()
	#bpf_update(delta)
	#bpf_draw()
	screen.draw_display()

screen.quit()
