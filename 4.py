"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
greatest = 0
for x in range(100,999):
	for y in range(100,999):
		palindrome = str(x*y)
		if palindrome == palindrome[::-1]:
			if int(palindrome) > greatest:
				greatest = int(palindrome)
print greatest