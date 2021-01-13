# Given a number n, print all primes smaller than or equal to n. 
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

from math import isqrt

# check prime
def is_prime(n : int) -> bool:
    if n < 2: 
        return False

    # only 2 is even number in all prime numbers
    if n == 2: 
        return True

    # if n is divisble by 2
    if n % 2 == 0:
        return False

    root = isqrt(n)
    # check only odd number
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    
    return True

# time is O(n*√n) | space is O(1)
def print_all_prime(number: int):

	for i in range(2, number+1):
		if is_prime(i):
			print(i, end=' ')
	print()

# Better Solution -> time is O(n*log(log(n))) | space is O(n)
def printAllPrimeNumbers(n):
    prime = [True]*(n+1)
    p = 2
    root = isqrt(n)

    # iterate over through root of n
    while p <= root:
        if prime[p] == True:
            # update multiples of current p
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    for i in range(2, n+1):
        if prime[i]:
            print(i, end=' ')
    print()

number = int(input())
print_all_prime(number)
printAllPrimeNumbers(number)