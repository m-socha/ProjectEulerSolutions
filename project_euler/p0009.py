PYTH_TRIPLET_SUM = 1000

for a in range(1, PYTH_TRIPLET_SUM - 2):
	for b in range(1, PYTH_TRIPLET_SUM - a):
		c = PYTH_TRIPLET_SUM - a - b
		if a**2 + b**2 == c**2:
			product = a*b*c
			print(product)
			break exit_loop

exit_loop:
