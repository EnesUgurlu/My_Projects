# This is an attempt to make a calculator for weapons in Dragalia Lost

def calculator():
	# type_wep = input('Do you want to craft a HDT or Agito weapon? ') # Assume Agito for now
	Agito_weapons_first_4 = {
		'Silver Masks': '40',
		'Gold Masks': '30',
		'Insanity': '0',
		'Sand': '1',
		'Orichalcum': '0',
		'Rupies': '2000000'
	}

	Agito_weapons_last_4 = {
		'Silver Masks': '16',
		'Gold Masks': '10',
		'Insanity': '7',
		'Sand': '0',
		'Orichalcum': '1',
		'Rupies': '7500000'
	}

	Agito_weapons_refinement = {
		'Silver Masks': '16',
		'Gold Masks': '10',
		'Insanity': '7',
		'Sand': '0',
		'Orichalcum': '1',
		'Rupies': '2500000'
	}

	result_dict = dict()
	check_wep = input('Have you crafted the base weapon? ')
	base_wep = None
	if check_wep.lower() == 'yes' or check_wep.lower() == 'y':
		base_wep = True
	elif check_wep.lower() == 'no' or check_wep.lower() == 'n':
		base_wep = False
	else:
		check_wep = input("Please enter 'yes' or 'no'.")

	curr_ub = int(input('How many unbinds does it have? '))
	desired_ub = int(input('How many unbinds do you want to end at? '))

	silver_masks = 0
	gold_masks = 0
	insanity = 0
	sand = 0
	orichalcum = 0
	rupies = 0

	if curr_ub >= desired_ub:
		return 'You have already reached or passed your target!'

	ref_status = str(input('Have you refined your weapon? '))

	if not base_wep:
		silver_masks += int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += int(Agito_weapons_first_4['Gold Masks'])
		insanity += int(Agito_weapons_first_4['Insanity'])
		sand += int(Agito_weapons_first_4['Sand'])
		orichalcum += int(Agito_weapons_first_4['Orichalcum'])
		rupies += int(Agito_weapons_first_4['Rupies'])

	if ref_status.lower() == 'n' or ref_status.lower() == 'no':
		silver_masks += int(Agito_weapons_refinement['Silver Masks'])
		gold_masks += int(Agito_weapons_refinement['Gold Masks'])
		insanity += int(Agito_weapons_refinement['Insanity'])
		sand += int(Agito_weapons_refinement['Sand'])
		orichalcum += int(Agito_weapons_refinement['Orichalcum'])
		rupies += int(Agito_weapons_refinement['Rupies'])

	# We only need the first 4 unbinds here
	if 0 <= curr_ub <= 4 and desired_ub <= 4:
		needed_ub_first_half = desired_ub - curr_ub
		silver_masks += needed_ub_first_half * int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += needed_ub_first_half * int(Agito_weapons_first_4['Gold Masks'])
		insanity += needed_ub_first_half * int(Agito_weapons_first_4['Insanity'])
		sand += needed_ub_first_half * int(Agito_weapons_first_4['Sand'])
		orichalcum += needed_ub_first_half * int(Agito_weapons_first_4['Orichalcum'])
		rupies += needed_ub_first_half * int(Agito_weapons_first_4['Rupies'])

	# We need both the first and last 4 unbinds here
	if 0 <= curr_ub <= 4 and desired_ub > 4:
		needed_ub_first_half = 4 - curr_ub
		silver_masks += needed_ub_first_half * int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += needed_ub_first_half * int(Agito_weapons_first_4['Gold Masks'])
		insanity += needed_ub_first_half * int(Agito_weapons_first_4['Insanity'])
		sand += needed_ub_first_half * int(Agito_weapons_first_4['Sand'])
		orichalcum += needed_ub_first_half * int(Agito_weapons_first_4['Orichalcum'])
		rupies += needed_ub_first_half * int(Agito_weapons_first_4['Rupies'])

		needed_ub_second_half = desired_ub - 4
		silver_masks += needed_ub_second_half * int(Agito_weapons_last_4['Silver Masks'])
		gold_masks += needed_ub_second_half * int(Agito_weapons_last_4['Gold Masks'])
		insanity += needed_ub_second_half * int(Agito_weapons_last_4['Insanity'])
		sand += needed_ub_second_half * int(Agito_weapons_last_4['Sand'])
		orichalcum += needed_ub_second_half * int(Agito_weapons_last_4['Orichalcum'])
		rupies += needed_ub_second_half * int(Agito_weapons_last_4['Rupies'])

	# We only need the second 4 unbinds here
	if curr_ub > 4 and desired_ub > 4:
		needed_ub_second_half = desired_ub - curr_ub
		silver_masks += needed_ub_second_half * int(Agito_weapons_last_4['Silver Masks'])
		gold_masks += needed_ub_second_half * int(Agito_weapons_last_4['Gold Masks'])
		insanity += needed_ub_second_half * int(Agito_weapons_last_4['Insanity'])
		sand += needed_ub_second_half * int(Agito_weapons_last_4['Sand'])
		orichalcum += needed_ub_second_half * int(Agito_weapons_last_4['Orichalcum'])
		rupies += needed_ub_second_half * int(Agito_weapons_last_4['Rupies'])


	result_dict['Silver Masks'] = silver_masks
	result_dict['Gold Masks'] = gold_masks
	result_dict['Insanity'] = insanity
	result_dict['Sand'] = sand
	result_dict['Orichalcum'] = orichalcum
	result_dict['Rupies'] = rupies

	return result_dict



def write_to_file():
	materials = calculator()
	with open('weapons.txt', 'w') as file:
		print(materials, file=file)

# I put this here because I keep forgetting to comment these lines out when testing
def run():
	my_dict = calculator()
	write_to_file()


def calculator_for_testing(check_wep, curr_ub, desired_ub, ref_status):
	# type_wep = input('Do you want to craft a HDT or Agito weapon? ') # Assume Agito for now

	# I use these dictionaries to look up the necessary amount of materials
	Agito_weapons_first_4 = {
		'Silver Masks': '40',
		'Gold Masks': '30',
		'Insanity': '0',
		'Sand': '1',
		'Orichalcum': '0',
		'Rupies': '2000000'
	}

	Agito_weapons_last_4 = {
		'Silver Masks': '16',
		'Gold Masks': '10',
		'Insanity': '7',
		'Sand': '0',
		'Orichalcum': '1',
		'Rupies': '7500000'
	}

	Agito_weapons_refinement = {
		'Silver Masks': '16',
		'Gold Masks': '10',
		'Insanity': '7',
		'Sand': '0',
		'Orichalcum': '1',
		'Rupies': '2500000'
	}

	result_dict = dict()
	base_wep = None
	if check_wep.lower() == 'yes' or check_wep.lower() == 'y':
		base_wep = True
	elif check_wep.lower() == 'no' or check_wep.lower() == 'n':
		base_wep = False
	else:
		return "Please enter 'yes' or 'no'."

	# Initialize values to 0 and add when necessary
	silver_masks = 0
	gold_masks = 0
	insanity = 0
	sand = 0
	orichalcum = 0
	rupies = 0

	if curr_ub >= desired_ub:
		return 'You have already reached or passed your target!'

	if not base_wep:
		silver_masks += int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += int(Agito_weapons_first_4['Gold Masks'])
		insanity += int(Agito_weapons_first_4['Insanity'])
		sand += int(Agito_weapons_first_4['Sand'])
		orichalcum += int(Agito_weapons_first_4['Orichalcum'])
		rupies += int(Agito_weapons_first_4['Rupies'])


	if ref_status.lower() == 'n' or ref_status.lower() == 'no':
		silver_masks += int(Agito_weapons_refinement['Silver Masks'])
		gold_masks += int(Agito_weapons_refinement['Gold Masks'])
		insanity += int(Agito_weapons_refinement['Insanity'])
		sand += int(Agito_weapons_refinement['Sand'])
		orichalcum += int(Agito_weapons_refinement['Orichalcum'])
		rupies += int(Agito_weapons_refinement['Rupies'])

	# We only need the first 4 unbinds here
	if 0 <= curr_ub <= 4 and desired_ub <= 4:
		needed_ub_first_half = desired_ub - curr_ub
		silver_masks += needed_ub_first_half * int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += needed_ub_first_half * int(Agito_weapons_first_4['Gold Masks'])
		insanity += needed_ub_first_half * int(Agito_weapons_first_4['Insanity'])
		sand += needed_ub_first_half * int(Agito_weapons_first_4['Sand'])
		orichalcum += needed_ub_first_half * int(Agito_weapons_first_4['Orichalcum'])
		rupies += needed_ub_first_half * int(Agito_weapons_first_4['Rupies'])

	# We need both the first and last 4 unbinds here
	if 0 <= curr_ub <= 4 and desired_ub > 4:
		needed_ub_first_half = 4 - curr_ub
		silver_masks += needed_ub_first_half * int(Agito_weapons_first_4['Silver Masks'])
		gold_masks += needed_ub_first_half * int(Agito_weapons_first_4['Gold Masks'])
		insanity += needed_ub_first_half * int(Agito_weapons_first_4['Insanity'])
		sand += needed_ub_first_half * int(Agito_weapons_first_4['Sand'])
		orichalcum += needed_ub_first_half * int(Agito_weapons_first_4['Orichalcum'])
		rupies += needed_ub_first_half * int(Agito_weapons_first_4['Rupies'])

		needed_ub_second_half = desired_ub - 4
		silver_masks += needed_ub_second_half * int(Agito_weapons_last_4['Silver Masks'])
		gold_masks += needed_ub_second_half * int(Agito_weapons_last_4['Gold Masks'])
		insanity += needed_ub_second_half * int(Agito_weapons_last_4['Insanity'])
		sand += needed_ub_second_half * int(Agito_weapons_last_4['Sand'])
		orichalcum += needed_ub_second_half * int(Agito_weapons_last_4['Orichalcum'])
		rupies += needed_ub_second_half * int(Agito_weapons_last_4['Rupies'])

	# We only need the second 4 unbinds here
	if curr_ub > 4 and desired_ub > 4:
		needed_ub_second_half = desired_ub - curr_ub
		silver_masks += needed_ub_second_half * int(Agito_weapons_last_4['Silver Masks'])
		gold_masks += needed_ub_second_half * int(Agito_weapons_last_4['Gold Masks'])
		insanity += needed_ub_second_half * int(Agito_weapons_last_4['Insanity'])
		sand += needed_ub_second_half * int(Agito_weapons_last_4['Sand'])
		orichalcum += needed_ub_second_half * int(Agito_weapons_last_4['Orichalcum'])
		rupies += needed_ub_second_half * int(Agito_weapons_last_4['Rupies'])

	result_dict['Silver Masks'] = silver_masks
	result_dict['Gold Masks'] = gold_masks
	result_dict['Insanity'] = insanity
	result_dict['Sand'] = sand
	result_dict['Orichalcum'] = orichalcum
	result_dict['Rupies'] = rupies

	return result_dict

if __name__ == "__main__":
	write_to_file()