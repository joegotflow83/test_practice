import unittest
from main import add, sub, conditional, is_prime


class TestMain(unittest.TestCase):


	# Test add really adds
	def test_add(self):

		self.assertEqual(add(2, 3), 5)

	# Test add raises error if not int
	def test_string_in_add(self):

		with self.assertRaises(TypeError):

			add('3', 3)

	# Test sub really subtracts
	def test_sub(self):

		self.assertEqual(sub(5, 2), 3)

	# Test sub raises error if not int
	def test_string_in_sub(self):

		with self.assertRaises(TypeError):

			sub('b', 3)

	# Test flow is correct
	def test_conditional(self):

		self.assertIn(conditional(22), 'You can drink')

	# Test if is_prime really runs correctly
	def test_is_prime(self):

		self.assertTrue(is_prime(5))

	# Test if the correct message is returned
	def test_right_message_returned(self):

		self.assertIn(is_prime(13), 'This number is prime')

	# Test only takes int
	def test_is_prime_only_int(self):

		with self.assertRaises(TypeError):

			is_prime('a')