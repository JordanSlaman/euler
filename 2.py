"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

total = 0
def z(x,y):
	global total
	if y > 4000000:
		print total
	else:
		if y %2 == 0:
			total += y
		newx = y
		newy = x+y
		z(newx,newy)
z(1,2)
