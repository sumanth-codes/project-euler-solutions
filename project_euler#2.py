def fibonacci():
	a,b = 1,2
	while 1:
		yield b
		a,b = b,a+b

g = fibonacci()
arr = list()
k = next(g)
while k<=4_000_000:
	if k%2==0:
		arr.append(k)
	k = next(g)
print(sum(arr))
