a = 600851475143
b = []
for i in range(1,a):
	if a%i == 0:
		if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
			b.append(i)

for num in b:
	print num