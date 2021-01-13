# check if the given number is prime or not
# https://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
# https://www.geeksforgeeks.org/primality-test-set-2-fermet-method/
# https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
# https://www.geeksforgeeks.org/primality-test-set-4-solovay-strassen/

# https://srtheme-bangla-programming.blogspot.com/2020/04/blog-post.html

from math import isqrt

# time is O(n) | space is O(1)
def is_prime(n : int) -> bool:
    if (n < 2):
        return False
    
    for i in range(2, n):
        if (n % i == 0):
            return False
    
    return True

# Efficient Solution -> time is O(√n) | space is O(1)
def isPrime(n : int) -> bool:
    if n < 2: 
        return False

    # only 2 is even number in all prime numbers
    if n == 2: 
        return True

    # when n is divisble by 2
    if n % 2 == 0:
        return False

    root = isqrt(n)
    # check only odd number
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    
    return True

if __name__ == '__main__':
    n = int(input())
    
    print(is_prime(n))
    print(isPrime(n))