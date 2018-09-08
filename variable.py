variables = {"table": "{0}"}
tables = [{"hi": "hello", "bye": "{1}"}, {"this": "2nd table"}]

def get_var(var):
	return variables[str(var)]

def set_var(var, val):
	variables[var] = val
	return val

def get_table(t):
	return tables[int(t)]
