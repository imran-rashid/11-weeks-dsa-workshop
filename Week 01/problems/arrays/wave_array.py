# Given a unsorted array arr[] of distinct integers. Sort the array into a wave-like array and return it.
# https://www.geeksforgeeks.org/sort-array-wave-form-2/
# https://practice.geeksforgeeks.org/problems/wave-array-1587115621/0/

# 1) Traverse all even positioned elements of input array, and do following.
# ….a) If current element is smaller than previous odd element, swap previous and current.
# ….b) If current element is smaller than next odd element, swap next and current.

# time is O(n) | Space is O(1)
def convertToWave(A,N):
	# only even numbers
    for i in range(0, N-1, 2):
    	# when current num is less than previous number
        if (i > 0 and (A[i] < A[i-1])):
            A[i], A[i-1] = A[i-1], A[i]
        # when current num is less than next number
        if (i < N-1 and (A[i] < A[i+1])):
            A[i], A[i+1] = A[i+1], A[i]

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()