from django.test import TestCase
from utils.random_string import generate_short


class RandomStringTests(TestCase):
	def test_utils_random_string_generate_short(self):
		print('Testing utils.random_string.generate_short()')
		random_string = generate_short()
		self.assertIsNotNone(random_string)

	def test_utils_random_string_generate_short_multiple(self):
		print('Testing utils.random_string.generate_short() MULTIPLE')
		random_strings = []
		for random_string in range(5000):
			random_strings.append(generate_short())
		random_string_set = set(random_strings)

		self.assertIsNotNone(random_strings)
		self.assertIsNotNone(random_string_set)
		self.assertEqual(len(random_string_set), len(random_strings))