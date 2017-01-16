#! /usr/bin/python

import unittest
from name_score import calculate_text_score, fetch_text_list, calculate_total_score

class TestNameScore(unittest.TestCase):

	def test_calculate_text_score_1(self):
		self.assertEqual(calculate_text_score('A'), 1)

	def test_calculate_text_score_2(self):
		self.assertEqual(calculate_text_score('ABC'), 1 + 2 + 3)

	def test_calculate_text_score_3(self):
		self.assertEqual(calculate_text_score('DEF'), 4 + 5 + 6)

	def test_fetch_text_list_1(self):
		filename_list = ['data1', 'data2']
		result_list = ['CDEF', 'ABC', 'FIJK', 'CDE', 'AB', 'FIJ']
		self.assertEqual(fetch_text_list(filename_list), result_list)

	def test_fetch_text_list_2(self):
		filename_list = ['data1']
		result_list = ['CDEF', 'ABC', 'FIJK']
		self.assertEqual(fetch_text_list(filename_list), result_list)

	def test_calculate_total_score_1(self):
		text_list = ['ABC', 'CDEF', 'FIJK']
		self.assertEqual(calculate_total_score(text_list), 150)


if __name__ == '__main__':
	unittest.main()
