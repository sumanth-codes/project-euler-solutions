def is_prime(n):
	if n==2:
		return 1
	elif n%2==0 or n == 1:
		return 0
	for t in range(3,int(n**0.5)+1,2):
		if n%t==0:
			return 0
	return 1

"""def primes(num):
	for i in range(1,num):
		if is_prime(i):
			yield i

prime_numbers = []
composites = []
for k in primes(100):
	prime_numbers.append(k)
for k in range(1,101):
	if not is_prime(k):
		composites.append(k)

print(prime_numbers)
print(composites)"""
def next_prime(num):
    num +=1
    while not is_prime(num):
        num += 1
    yield num

def nth_prime(n):
    primes = {1:2}
    for i in range(2,n+1):
        primes[i] = next_prime(primes[i-1])
    return primes[n]

# print(nth_prime(10001))
for i in nth_prime(10001):
	print(i)