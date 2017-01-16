#! /usr/bin/python

import unittest
from perfect_number import is_perfect

class TestPerfectNumber(unittest.TestCase):
	
	def test_is_perfect_1(self):
		self.assertEqual(is_perfect(6), True)

	def test_is_perfect_2(self):
		self.assertEqual(is_perfect(28), True)

	def test_is_perfect_3(self):
		self.assertEqual(is_perfect(33550336), True)

	def test_is_perfect_4(self):
		self.assertEqual(is_perfect(10000), False)


if __name__ == '__main__':
	unittest.main()
