
def fib():
	a,b = 0,1
	while True:
		yield b
		a,b = b,a+b 

f = fib()
print([f.next() for i in range(10)])
