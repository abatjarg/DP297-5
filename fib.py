def fib(a):
	if( a <= 1):
		return a
	else:
		return fib(a-1) + fib(a-2)

if __name__ == "__main__":
	i = 1
	b = 0;
	while fib(i) < 4000001:
		if fib(i)%2 == 0:
			b = b + fib(i)
			print fib(i)
		i = i + 1

	print "Sum: %d" %b
		
