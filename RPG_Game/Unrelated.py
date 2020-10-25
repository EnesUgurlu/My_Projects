def get_number(prompt):
	if prompt == 'Please input the first number:':
		try:
			num_1 = input(prompt)
			num_1 = float(num_1)
		except ValueError:
			print('The input should be a number.')
			get_number('Please input the first number:')

	try:
		num_2 = input('Please input the second number:')
		num_2 = float(num_2)
	except ValueError:
		print('The input should be a number.')
		get_number('Please input the second number:')

	return (num_1, num_2)

get_number('Please input the first number:')