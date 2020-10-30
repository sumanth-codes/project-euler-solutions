# multiples of 3
# 3,6,9,12,15,18,21,.....,993,996,999
# multiples of 5
# 5,10,15,20,25,.....,985,990,995
# multiples of 15
# 15,30,45,60,......,960,975,990

# as sum of terms in an arithmetic progression is (a+l)*n/2
# here a--first term 
#      l--last term
#      n--no. of terms

multiple_3 = (3+999)*333//2 
multiple_5 = (5+995)*199//2
multiple_15 = (15+990)*66//2

print(multiple_3+multiple_5-multiple_15)
