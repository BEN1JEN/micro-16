import variable
import engine
import prameter
import util
import evaluate
program_counter = 0

def execute_command(line):
	command, pram_start = util.get_until(line, "\(")
	command = util.discard(command, " ")
	prams = line[pram_start:]
	prams, t = util.get_until(prams, "\):?$")
	if len(prams) > 0:
		prams = util.seperate(prams, ",")
		for i, pram in enumerate(prams):
			prams[i] = evaluate.expression(prameter.calc_alternitives_for_pram(prameter.clean_pram(pram)))
	end = line[-1:] == ":"

	if command == "print":
		return engine.display_print(prams[0], prams[1], prams[2])
	elif command == "twentynine":
		return 29
	elif command == "py_print":
		print(prams)

def execute_set_variable(line):
	line = prameter.calc_alternitives_for_pram(prameter.clean_pram(line))
	var, exp_start = util.get_until(line, "[\+\*\-\/]?=")
	exp = line[exp_start:]
	val = evaluate.expression(exp)

	variable.set_var(var, val)
