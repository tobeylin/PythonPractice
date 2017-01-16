#! /usr/bin/python

def is_perfect(number):
	sum = 1
	for positive_factor in range(2, number/2 + 1):
		if(number % positive_factor == 0):
			sum += positive_factor
	return sum == number


if __name__ == '__main__':
	number = int(raw_input('enter a number: '))
	print is_perfect(number)
