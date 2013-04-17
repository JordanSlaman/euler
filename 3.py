"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143
check = 2

while check*2 <= num:
	if num%check == 0:
		num = num/check
	else:
		check+=1
print num