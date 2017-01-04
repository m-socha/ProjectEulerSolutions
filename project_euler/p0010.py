from lib.math_helper import is_prime

MAX_PRIME = 2000000

prime_sum = 0
for x in range(1, MAX_PRIME):
	if is_prime(x):
		prime_sum += x

print(prime_sum)
