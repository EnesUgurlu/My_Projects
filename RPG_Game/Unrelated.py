import math

# listy = []
#
# for i in range(16):
# 	listy.append(i)
#
# for i, j in enumerate(listy):
# 	print(i, math.factorial(j))
#
# print('\n')
# print("Testing some numbers")
#
# numbers = [1, 4, 5, 9, 10, 11, 15]
#
# for num in numbers:
# 	print(str(num) + '! has ' + str(num//5) + ' zeroes')

def roman(n):
	whole = ''


	if n >= 5:
		whole += 'V'
		n -= 5
	if n >= 4:
		whole += 'IV'
		n -= 4
	if n >= 3:
		whole += 'III'
		n -= 3
	if n >= 2:
		whole += 'II'
		n -= 2
	if n >= 1:
		whole += 'I'
		n -= 1

	return whole

print(roman(8))

