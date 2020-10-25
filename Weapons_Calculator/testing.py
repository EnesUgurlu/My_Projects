from unittest.mock import patch
import unittest
from Weapons_Calculator.Main import calculator_for_testing


class TestOne(unittest.TestCase):
	def test_check_materials(self):
		self.assertEqual(calculator_for_testing('y', 0, 4, 'y'), {'Silver Masks': 160, 'Gold Masks': 120,
																	'Insanity': 0, 'Sand': 4,
																	'Orichalcum': 0, 'Rupies': 8000000})
		self.assertEqual(calculator_for_testing('y', 0, 8, 'n'), {'Silver Masks': 240, 'Gold Masks': 170,
																	'Insanity': 35, 'Sand': 4, 'Orichalcum': 5,
																	'Rupies': 40500000})
		self.assertEqual(calculator_for_testing('y', 2, 6, 'n'), {'Silver Masks': 128, 'Gold Masks': 90,
																	'Insanity': 21, 'Sand': 2, 'Orichalcum': 3,
																	'Rupies': 21500000})
		self.assertEqual(calculator_for_testing('y', 4, 5, 'n'), {'Silver Masks': 32, 'Gold Masks': 20,
																	'Insanity': 14, 'Sand': 0, 'Orichalcum': 2,
																	'Rupies': 10000000})
		self.assertEqual(calculator_for_testing('n', 0, 8, 'n'), {'Silver Masks': 280, 'Gold Masks': 200,
																	'Insanity': 35, 'Sand': 5, 'Orichalcum': 5,
																	'Rupies': 42500000})
class TestTwo(unittest.TestCase):
	def test_target_reached(self):
		self.assertEqual(calculator_for_testing('n', 6, 3, 'y'), 'You have already reached or passed your target!')
		self.assertNotEqual(calculator_for_testing('n', 6, 3, 'y'), 'You have already reached or passed your target')

class TestThree(unittest.TestCase):
	def test_abnormal_inputs(self):
		self.assertEqual(calculator_for_testing('a', 1, 1, 'y'), "Please enter 'yes' or 'no'.")



suite1 = unittest.TestLoader().loadTestsFromTestCase(TestOne)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTwo)
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestThree)

alltests = unittest.TestSuite([suite1, suite2, suite3])