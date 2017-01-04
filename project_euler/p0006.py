MAX_NUM = 100

square_sum = sum(range(MAX_NUM + 1))**2
sum_squares = sum(x**2 for x in range(MAX_NUM + 1))
difference = square_sum - sum_squares

print(difference)
