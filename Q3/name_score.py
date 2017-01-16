#! /usr/bin/python

import sys
import re


def fetch_text_list(filename_list): 
	text_list = []
	for filename in filename_list:
		with open(filename, 'r') as data_file:
			file_text = data_file.read()
			tmp_text_list = re.findall('[A-Z]+', file_text)
			text_list += tmp_text_list

	return text_list


def calculate_text_score(text):

	base = ord('A')
	text_score = 0
	for char in text:
		char_score = ord(char) - base + 1
		text_score += char_score
	return text_score


def calculate_total_score(text_list):
	total_score = 0
	for index, text in enumerate(text_list):
		text_score = calculate_text_score(text)
		weight = index + 1
		total_score += text_score * weight
	return total_score


if __name__ == '__main__':
	
	filename_list = sys.argv[1:]
	text_list = fetch_text_list(filename_list)
	text_list.sort()
	print calculate_total_score(text_list)
