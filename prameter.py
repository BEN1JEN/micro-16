import re
import bpf
import variable

def clean_pram(pram):
	to_erase = []
	for i, c in enumerate(pram):
		if c == " " or c == "\t":
			erase = True
			strings = re.finditer(r"[a-zA-Z][a-zA-Z ]*[a-zA-Z]", pram)
			for s in strings:
				if i >= s.start() and i < s.end():
					erase = False
			if erase:
				to_erase.append(i)

	clean_pram = pram
	for pos in reversed(to_erase):
		clean_pram = clean_pram[:pos] + clean_pram[pos+1:]

	return clean_pram

def calc_alternitives_for_pram(pram):
	alt_pram = re.sub(r"~([a-zA-Z][a-zA-Z ]*[a-zA-Z])", replace_var, pram)
	alt_pram = re.sub(r"[a-zA-Z][a-zA-Z ]*[a-zA-Z]\(.*?\)", replace_cmd, alt_pram)
	return alt_pram

def replace_var(m):
	return str(variable.get_var(m.group(1)))

def replace_cmd(m):
	return str(bpf.execute_command(m.group(0)))
