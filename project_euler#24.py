from itertools import permutations
count =0
for i in list(permutations('0123456789',10)):
	count += 1
	if count == 1_000_000:
		break
print(i)