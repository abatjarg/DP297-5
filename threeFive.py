a = []
b = 0

for i in range(1000):
	if i % 5 == 0:
		a.append(i)
	elif i % 3 == 0:
		a.append(i)

for i in a:
	b += i

print "Sum: %d" %b