import math
listy = []

for i in range(16):
	listy.append(i)

for i, j in enumerate(listy):
	print(i, math.factorial(j))

print('\n')
print("Testing some numbers")

numbers = [1, 4, 5, 9, 10, 11, 15]

for num in numbers:
	print(str(num) + '! has ' + str(num//5) + ' zeroes')
