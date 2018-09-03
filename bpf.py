import variable
from engine import *
from pram import *
from util import *
import evaluate
program_counter = 0

def execute_command(line):
	command, pram_start = get_until(line, "\(")
	command = discard(command, " ")
	prams = line[pram_start:]
	prams, t = get_until(prams, "\):?$")
	if len(prams) > 0:
		prams = seperate(prams, ",")
		for i, pram in enumerate(prams):
			prams[i] = evaluate.expression(calc_alternitives_for_pram(clean_pram(pram)))
	end = line[-1:] == ":"

	if command == "print":
		return display_print(prams[0], prams[1], prams[2])
	if command == "twentynine":
		return 29
