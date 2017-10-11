def fib(max):
	n, a, b = 0, 0, 1
	while(n<max):
		yield b
		a, b = b, a+b
		#yield b
		n = n+1
	return

generator = fib(8)
for i in generator:
	print i
