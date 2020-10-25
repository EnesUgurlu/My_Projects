# This is an attempt to make a calculator for weapons in Dragalia Lost

def calculator():
	# type_wep = input('Do you want to craft a HDT or Agito weapon? ') # Assume Agito
	check_wep = input('Have you crafted the base weapon? ')
	if check_wep.lower() == 'yes' or 'y':
		curr_ub = int(input('How many unbinds does it have? '))
		desired_ub = int(input('How many unbinds do you want to end at? '))
		needed_ub = desired_ub - curr_ub
		# Input the necessary materials here
		one_to_four_silver_mask = (needed_ub - 4) * 40
		five_to_eight_silver_mask = needed_ub * 16
		refine_silver_mask = 16

		if curr_ub >= desired_ub:
			print('You have more unbinds than you wanted!')
			return
		if needed_ub >= 4:
			# Here we need the 5-8 unbind materials
			print(f'{five_to_eight_silver_mask} Silver Masks needed for the last 4 unbinds')
			print(f'{refine_silver_mask} Silver Masks needed for refinement')

		total_silver_masks = one_to_four_silver_mask + five_to_eight_silver_mask + refine_silver_mask
		print(f'{one_to_four_silver_mask} Silver Masks needed for the first 4 unbinds')
		print(f'{total_silver_masks} Silver Masks needed total')


	# We need one more 'lower unbind' materials here, I will add it manually
	elif check_wep.lower() == 'no' or 'n':
		desired_ub = int(input('How many unbinds do you want to end at? '))
		needed_ub = desired_ub + 1 # +1 lower_unbind


calculator()

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