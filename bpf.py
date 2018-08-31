from engine import *
from util import *

program_counter = 0

def execute_command(screen, line):
	line = discard(line, " ")
	command, pram_start = get_until(line, "(")
	prams = line[pram_start:]
	prams, t = get_until(prams, ")")
	prams = seperate(prams, ",")
	end = line[-1:] == ":"

	if command == "print":
		display_print(screen, prams[1], prams[2], prams[3])
