

def line_conf():
	b = 15
	def line(x):
		return 2*x+b
	return line

a_line = line_conf()
print(a_line(10))
