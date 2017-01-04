from lib.math_helper import is_prime

TARGET_PRIMES_FOUND = 10001

num_primes_found = 0
current_num = 1
while num_primes_found < TARGET_PRIMES_FOUND:
	current_num += 1
	if is_prime(current_num):
		num_primes_found += 1

print(current_num)
