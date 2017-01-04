MAX_DIV_NUM = 20

divisible_num = 20
while any(divisible_num % x != 0 for x in range(1, MAX_DIV_NUM + 1)):
	divisible_num += MAX_DIV_NUM

print(divisible_num)
