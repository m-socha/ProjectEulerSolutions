MAX_TERM = 4000000

prev_term = 1
current_term = 2

sum_within_max_term = 0
while current_term <= MAX_TERM:
	if current_term % 2 == 0:
		sum_within_max_term += current_term
	prev_term, current_term = current_term, prev_term + current_term

print(sum_within_max_term)
