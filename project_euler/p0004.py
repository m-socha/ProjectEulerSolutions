from lib.math_helper import is_palindrome

UPPER_BOUND = 1000
LOWER_BOUND = 100

largest_palindrome = 0
for num1 in range(LOWER_BOUND, UPPER_BOUND):
	for num2 in range(LOWER_BOUND, UPPER_BOUND):
		product = num1 * num2
		if product > largest_palindrome and is_palindrome(product):
			largest_palindrome = product

print(largest_palindrome)
