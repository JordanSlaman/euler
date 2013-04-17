"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def isprime(n):
	n*=1.0
	for x in range(2, int(n**0.5)+1):
		if n/x == int(n/x):
			return False
	return True

count = 0
x=2
while True:
	if isprime(x):
		count+=1
		#print str(count) + ": " + str(x)
		if count == 10001:
			print x
			break
	x+=1
