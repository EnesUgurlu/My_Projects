# Inspired by the EPICRPG Discord bot
import random


print('Welcome to this text based RPG!\n'
	  "You can start by typing 'start'.\n")

user_input = input()
playing = False

list_of_options = "You can type the following commands: \n" \
				"'fish' to catch some fish \n" \
				"'inventory' to look at your items \n" \
				"'meat' to hunt animals for meat \n"

if user_input == 'start':
	print('You have started this adventure!')
	playing = True

inventory = dict()

while playing:
	print(list_of_options)
	user_input = input()

	if user_input == 'fish':
		amount = random.randint(1, 3)
		print(f'You have caught {amount} fish!')
		if 'fish' not in inventory:
			inventory['fish'] = amount
		else:
			new_amount = amount + int(inventory['fish'])
			inventory['fish'] = new_amount

	if user_input == 'inventory':
		print(inventory)

	if user_input == 'hunt':
		amount = random.randint(1, 5)
		print(f'You got {amount} slabs of meat!')
		if 'meat' not in inventory:
			inventory['meat'] = amount
		else:
			new_amount = amount + int(inventory['meat'])
			inventory['meat'] = new_amount