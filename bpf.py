from engine import *
from util import *
from pram import *
import evaluate

variables = {}
program_counter = 0

def execute_command(screen, line):
	command, pram_start = get_until(line, "\(")
	command = discard(command, " ")
	prams = line[pram_start:]
	prams, t = get_until(prams, "\)(?::|$)")
	prams = seperate(prams, ",")
	end = line[-1:] == ":"

	for i, pram in enumerate(prams):
		prams[i] = evaluate.expression(calc_alternitives_for_pram(clean_pram(pram)))

	if command == "print":
		display_print(screen, prams[0], prams[1], prams[2])
