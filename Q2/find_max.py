#! /usr/bin/python

import sys


def get_max_number(number_list, bound):
	window_size = 1
	for number_index in range(len(number_list)):
		number_value = number_list[number_index]	
		for compare_index in range(window_size):
			compare_value = number_list[compare_index]
			if number_value > compare_value:
				number_list[compare_index], number_list[number_index] = number_list[number_index], number_list[compare_index]
				number_value = compare_value
		window_size = window_size + 1 if window_size < bound else bound
	return number_list[:bound]


def get_number_list(filename):
	with open(filename, 'r') as data_file:
		number_str = data_file.read()
		number_list = number_str.split('\n')
		number_list = map(lambda number: int(number), number_list)
		return number_list


if __name__ == '__main__':

	number_list = get_number_list(sys.argv[1])
	max_number_list = get_max_number(number_list, 3)

	for number in max_number_list:
		print number
