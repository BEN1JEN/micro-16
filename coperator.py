import re
import math

def cequal(val1, val2):
	return convert(val1) == convert(val2)

def reference_equal(val1, val2):
	return val1 is val2

def greater_then(val1, val2):
	return convert(val1, True) > convert(val2, True)

def greater_then_or_equal(val1, val2):
	return convert(val1, True) >= convert(val2, True)

def cadd(val1, val2):
	return convert(val1, True) + convert(val2, True)

def csubtract(val1, val2):
	return convert(val1, True) - convert(val2, True)

def cmultiply(val1, val2):
	return convert(val1, True) * convert(val2, True)

def cdevide(val1, val2):
	return convert(val1, True) / convert(val2, True)

def cmodulo(val1, val2):
	return convert(val1, True) % convert(val2, True)

def cpower(val1, val2):
	return pow(convert(val1, True), convert(val2, True))

def croot(val1, val2):
	return pow(convert(val2, True), 1/convert(val2, True))

def clog(val1, val2):
	return math.log(convert(val2, True), convert(val1, True))

def cand(val1, val2):
	return is_true(val1) and is_true(val2)

def cor(val1, val2):
	return is_true(val1) or is_true(val2)

def cxor(val1, val2):
	bool1 = is_true(val1)
	bool2 = is_true(val2)
	return (bool1 or bool2) and not (bool1 and bool2)

def convert(val, force_num=False):
	if type(val) == dict:
		new_val = {}
		for key, thing in enumerate(val):
			new_val[convert(key)] = convert(thing)
	else:
		new_val = str(val)
		if re.search("^[0-9\.]+$", new_val):
			new_val = float(new_val)

	if force_num and (type(new_val) is not float):
		if (type(new_val) == str) or (type(new_val) == dict):
			new_val = len(new_val)
		elif type(new_val) == bool:
			if val:
				new_val = 1
			else:
				new_val = 0

	return new_val

def is_true(val):
	if type(val) is bool:
		return val

	if type(val) is float:
		return val != 0

	if type(val) is str:
		if val == "false" or val == "False" or val == "FALSE":
			return False
		if val == "true" or val == "True" or val == "TRUE":
			return True

	if type(val) is str or type(val) is dict:
		return len(val) != 0
