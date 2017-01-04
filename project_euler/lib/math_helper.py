def is_prime(num):
	if num < 2:
		return False

	factor = 2
	while factor * factor <= num:
		if num % factor == 0:
			return False
		factor += 1
	return True

def is_palindrome(num):
	return str(num) == str(num)[::-1]
