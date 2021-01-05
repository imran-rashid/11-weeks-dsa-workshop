# Given an array A of positive integers. Your task is to find the leaders in the array.  
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/0/
# https://www.geeksforgeeks.org/leaders-in-an-array/

# time is O(n) | Space is O(1)
def leaders(A, N):
    list_of_leaders = []

    if N == 0 or N == 1:
        return A
    
    max_from_right = A[N-1]
    for i in range(len(A)-1, -1, -1): # N-1 to 0
        if max_from_right <= A[i]:
            max_from_right = A[i]
            list_of_leaders.append(max_from_right)
    
    list_of_leaders.reverse() # in place
    return list_of_leaders

import math
def main():
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        A=leaders(A,N)

        for i in A:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
