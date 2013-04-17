"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
num = 2520
while True:
	fail = False
	for x in range(1,20):
		if num%x != 0:
			fail = True
	if not fail:
		print num
		break
	else:
		num += 2520
