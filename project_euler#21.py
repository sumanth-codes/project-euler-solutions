def sum_of_divisors(num):
	sumdiv = 0
	for i in range(1,num//2+1):
		if num % i == 0:
			sumdiv += i
	return sumdiv


amicables = set()

for number in range(1,10000):
	k = sum_of_divisors(number)
	num2 = sum_of_divisors(k)
	if k<10000:
		if number == num2 and number != k:
			amicables.add(number)
			amicables.add(k)

print(sum(amicables))