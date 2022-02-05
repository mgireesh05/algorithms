import time
from math import ceil

def karatsuba_mul(x, y):
	if x < 10 or y < 10:
		return x * y

	lx = len(str(x))
	ly = len(str(y))

	n = max(lx, ly)
	n2 = int(ceil(n/2.0))

	a = x / 10**(n2)
	b = x % 10**(n2)
	c = y / 10**(n2)
	d = y % 10**(n2)

	ac = karatsuba_mul(a, c)
	bd = karatsuba_mul(b, d)
	ad_bc = karatsuba_mul(a+b, c+d)  - ac - bd
	pn = 10**(2*n2)
	pn2 = 10**n2

	return (pn * ac) + (pn2 * (ad_bc)) + bd

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

start = int(round(time.time() * 1000))
for i in range(1000):
	mul = karatsuba_mul(x, y)

if mul != x * y:
	print ("Wrong: Correct answer is " + str(x*y))
else:
	cur = int(round(time.time() * 1000))
	print ("Ans: " + str(mul) + " -> done in " + str(cur - start) + " millisecs")
