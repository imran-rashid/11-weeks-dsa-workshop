# Given an array A of N positive numbers. The task is to find the first Equilibrium Point in the array. 
# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
# https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/

import math

# time is O(n) | Space is O(1)
def equilibriumPoint(A, N):
    if (N == 1): return 1
    
    left_sum = 0
    total_sum = sum(A)
    
    for i, num in enumerate(A):
        total_sum -= num
        
        if total_sum == left_sum: 
            return i+1
        left_sum += num
    
    return -1

def main():
    T = int(input())
    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        print(equilibriumPoint(A, N))
        T -= 1

if __name__ == "__main__":
    main()
