from util import *
import re
import math
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
		elif re.search("^[\d\.]+$", thing):
			num_stack.append(thing)
		elif re.search("^\D=?$", thing):
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
	matches = re.finditer(r"[\d\.]+|\D=?", exp)
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
		return 1
	elif op == "*" or op == "/" or op == "%":
		return 2
	elif op == "^" or op == "root" or op == "log":
		return 3
	elif op == "=" or op == "==" or op == "!=" or op == "!==":
		return 4
	elif op == ">" or op == "<" or op == ">=" or op == "<=" or op == "=>" or op == "=<":
		return 4
	elif op == "!>" or op == "!<" or op == "!>=" or op == "!<=" or op == "!=>" or op == "!=<":
		return 4
	elif op == "and" or op == "&" or op == "or" or op == "|" or op == "xor" or op == "$":
		return 5
	elif op == "nand" or op == "!&" or op == "nor" or op == "!|" or op == "xnor" or op == "!$":
		return 5

def calculate_op(num1, num2, op):
	if op == "=" or op == "==":
		return num1 == num2
	elif op == ">" or op == "!<=" or op == "!=<":
		return num1 > num2
	elif op == "<" or op == "!>=" or op == "!=>":
		return num1 < num2
	elif op == ">=" or op == "=>" or op == "!<":
		return num1 >= num2
	elif op == "<=" or op == "=<" or op == "!>":
		return num1 <= num2
	elif op == "and" or op == "&":
		return num1 and num2
	elif op == "or" or op == "|":
		return num1 or num2
	elif op == "xor" or op == "$":
		return (num1 or num2) and not (num1 and num2)
	elif op == "nand" or op == "!&":
		return not (num1 and num2)
	elif op == "nor" or op == "!|":
		return not (num1 or num2)
	elif op == "nxor" or op == "!$":
		return not ((num1 or num2) and not (num1 and num2))

	num1 = float(num1)
	num2 = float(num2)

	if op == "+":
		return num1+num2
	elif op == "-":
		return num1-num2
	elif op == "*":
		return num1*num2
	elif op == "%":
		return num1%num2
	elif op == "^":
		return pow(num1, num2)
	elif op == "root":
		return pow(num2, 1/num1)
	elif op == "log":
		return math.log(num2, num1)

print(expression("4-2*2"))
