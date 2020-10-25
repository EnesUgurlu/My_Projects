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
	result_dict = dict()
	check_wep = input('Have you crafted the base weapon? ')
	if check_wep.lower() == 'yes' or 'y':

		curr_ub = int(input('How many unbinds does it have? '))
		desired_ub = int(input('How many unbinds do you want to end at? '))
		ref_status = str(input('Have you refined your weapon? '))
		silver_masks = 0

		if ref_status.lower() == 'n' or 'no':
			silver_masks += int(Agito_weapons_first_4['Silver Masks'])

		if curr_ub >= desired_ub:
			print('You have more unbinds than you wanted!')
			return

		if 0 <= curr_ub <= 4:
			needed_ub_first_half = 4 - curr_ub
			silver_masks += needed_ub_first_half * int(Agito_weapons_first_4['Silver Masks'])
			needed_ub_second_half = desired_ub - 4
			silver_masks += needed_ub_second_half * int(Agito_weapons_last_4['Silver Masks'])


		result_dict['Silver Masks'] = silver_masks

	return result_dict

	# We need one more 'lower unbind' materials here, I will add it manually
	# elif check_wep.lower() == 'no' or 'n':
	# 	desired_ub = int(input('How many unbinds do you want to end at? '))
	# 	needed_ub = desired_ub + 1 # +1 lower_unbind


print(calculator())





# Materials for Agito:
# Base weapon:
# 40 Silver Masks
# 30 Golden Masks
# 0 Insanity
# 1 Sand
# 0 Orichalcum
# 2,000,000 (2M) rupies

# First 4 Unbinds:
# 40 Silver Masks
# 30 Golden Masks
# 0 Insanity
# 1 Sand
# 0 Orichalcum
# 2,000,000 (2M) rupies

# Last 4 Unbinds:
# 16 Silver Masks
# 10 Golden Masks
# 7 Insanity
# 0 Sand
# 1 Orichalcum
# 7,500,000 (7.5M) rupies

# Refinement needs:
# 16 Silver Masks
# 10 Golden Masks
# 7 Insanity
# 0 Sand
# 1 Orichalcum
# 2,500,000 (2.5M) rupies