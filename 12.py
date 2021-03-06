"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import itertools

def gen_triangle_number():
	for n in itertools.count(2):
		yield sum(range(n))

def get_divisors(num):
	divisors = []
	for n in range(1, num+1):
		if num % n == 0:
			divisors.append(n)
	return divisors

triangle = gen_triangle_number()

for x in itertools.count(1):
	t = triangle.next()
	if len(get_divisors(t)) > 500:
		print t, get_divisors(t)
		break