# Given a number n, find the sum of first natural numbers
# https://www.geeksforgeeks.org/program-find-sum-first-n-natural-numbers/

# Method 1: time is O(n) | space is O(1)
def findSum(n : int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Method 2: time is O(1) | space is O(1)
def findSum2(n : int) -> int:
    return (n*(n+1)) // 2

# Method 3: time is O(n) | space is O(n)
def findSum3(n : int) -> int:
    if (n == 0):
        return 0
    return n + findSum3(n-1)

# Efficient solution time is O(1) | space is O(1) [avoid overflow error]
def Sum(n : int) -> int:
    if n % 2 == 0:
        return (n // 2) * (n + 1)
    return n * ((n+1)//2)

if __name__ == '__main__':
    number = int(input('Enter Natural number: '))

    print(f'sum is {findSum(number)}')
    print(f'sum is {findSum2(number)}')
    print(f'sum is {findSum(number)}')
    print(f'sum is {Sum(number)}')