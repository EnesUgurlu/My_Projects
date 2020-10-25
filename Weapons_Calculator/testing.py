from unittest.mock import patch
from unittest import TestCase
# from Weapons_Calculator.Main import calculator



class Test(TestCase):

	for input_case, output_expected in input_output_dict.items():
		output_actual = Main.calculator()
		self.assertEqual(output_expected, output_actual)