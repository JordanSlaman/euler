"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def isprime(n):
	n*=1.0
	for x in range(2, int(n**0.5)+1):
		if n/x == int(n/x):
			return False
	return True

sumOfPrimes = 0
for x in range(2, 2000000):
	if isprime(x):
		sumOfPrimes += x
print sumOfPrimes