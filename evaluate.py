from util import *
import re
import coperator as o

def expression(exp):
	op_stack = []
	num_stack = []
	exp = seperate_exp(exp)

	for thing in exp:
		if thing == ")":
			while len(op_stack) != 0 and op_stack[-1] != "(":
				num2 = num_stack.pop()
				num1 = num_stack.pop()
				num = calculate_op(num1, num2, op_stack.pop())
				num_stack.append(num)
			op_stack.pop()
		elif re.search("^[0-9a-zA-Z \.]+$", thing):
			num_stack.append(thing)
		elif re.search("^[^0-9a-zA-Z \.][=><]?$", thing):
			while len(op_stack) != 0 and cmp_op_order(op_stack[-1], thing):
				num2 = num_stack.pop()
				num1 = num_stack.pop()
				num = calculate_op(num1, num2, op_stack.pop())
				num_stack.append(num)
			op_stack.append(thing)

	while len(op_stack)!=0:
		num2 = num_stack.pop()
		num1 = num_stack.pop()
		num = calculate_op(num1, num2, op_stack.pop())
		num_stack.append(num)

	return num_stack[0]

def seperate_exp(exp):
	matches = re.finditer(r"[0-9a-zA-Z \.]+|[^0-9a-zA-Z \.][=><]?", exp)
	output = []
	for match in matches:
		output.append(match.group(0))
	return output

def cmp_op_order(op1, op2):
	return get_op_order(op1) >= get_op_order(op2)

def get_op_order(op):
	if op == "(":
		return 0
	elif op == "+" or op == "-":
		return 3
	elif op == "*" or op == "/" or op == "%":
		return 4
	elif op == "^" or op == "root" or op == "log":
		return 5
	elif op == "=" or op == "==" or op == "$" or op == "$=" or op == "!=" or op == "!==" or op == "!$" or op == "!$=":
		return 2
	elif op == ">" or op == "<" or op == ">=" or op == "<=" or op == "=>" or op == "=<":
		return 2
	elif op == "!>" or op == "!<" or op == "!>=" or op == "!<=" or op == "!=>" or op == "!=<":
		return 2
	elif op == "and" or op == "&" or op == "or" or op == "|" or op == "xor" or op == "$":
		return 1
	elif op == "nand" or op == "!&" or op == "nor" or op == "!|" or op == "xnor" or op == "!$":
		return 1

def calculate_op(val1, val2, op):
	if op == "=" or op == "==":
		return o.cequal(val1, val2)
	elif op == "$" or op == "$=":
		return o.reference_equal(val1, val2)
	elif op == "!=" or op == "!==":
		return not o.cequal(val1, val2)
	elif op == "!$" or op == "!$=":
		return not o.reference_equal(val1, val2)
	elif op == ">" or op == "!<=" or op == "!=<":
		return o.greater_then(val1, val2)
	elif op == "<" or op == "!>=" or op == "!=>":
		return o.greater_then(val2, val1)
	elif op == ">=" or op == "=>" or op == "!<":
		return o.greater_then_or_equal(val1, val2)
	elif op == "<=" or op == "=<" or op == "!>":
		return o.greater_then_or_equal(val2, val1)
	elif op == "and" or op == "&":
		return o.cand(val1, val2)
	elif op == "or" or op == "|":
		return o.cor(val1, val2)
	elif op == "xor" or op == "$":
		return o.cxor(val1, val2)
	elif op == "nand" or op == "!&":
		return not o.cand(val1, val2)
	elif op == "nor" or op == "!|":
		return not o.cor(val1, val2)
	elif op == "nxor" or op == "!$":
		return not o.cxor(val1, val2)
	if op == "+":
		return o.cadd(val1, val2)
	elif op == "-":
		return o.csubtract(val1, val2)
	elif op == "*":
		return o.cmultiply(val1, val2)
	elif op == "%":
		return o.cmodulo(val1, val2)
	elif op == "^":
		return o.cpower(val1, val2)
	elif op == "root":
		return o.croot(val1, val2)
	elif op == "log":
		return o.clog(val1, val2)
