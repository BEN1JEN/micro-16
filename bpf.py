from engine import *
from util import *

variables = {}
program_counter = 0

def execute_command(screen, line):
	command, pram_start = get_until(line, "(")
	command = discard(command, " ")
	prams = line[pram_start:]
	prams, t = get_until(prams, ")")
	prams = seperate(prams, ",")
	end = line[-1:] == ":"

	if command == "print":
		display_print(screen, prams[0], prams[1], prams[2])
