from lib.math_helper import is_prime

LARGE_PRIME = 600851475143

unfactored_value = LARGE_PRIME
while not is_prime(unfactored_value):
	factor = 2
	while unfactored_value % factor != 0:
		factor += 1
	unfactored_value //= factor

print(unfactored_value)
