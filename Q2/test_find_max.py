#! /usr/bin/python

import unittest
from find_max import get_number_list, get_max_number


class TestFindMax(unittest.TestCase):

	def test_get_number_list_1(self):
		filename = 'data'
		result_number_list = [2134, 3412, 6421, 8723, 9239, 1234, 2345]
		self.assertEqual(get_number_list(filename), result_number_list)

	def test_get_max_number(self):
		number_list = [2134, 3412, 6421, 8723, 9239, 1234, 2345]
		self.assertEqual(get_max_number(number_list, 3), [9239, 8723, 6421])


if __name__ == '__main__':
	unittest.main()
