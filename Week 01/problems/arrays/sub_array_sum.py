# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
# https://www.geeksforgeeks.org/find-subarray-with-given-sum/
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/0/

# time is O(n) | space is O(1)
def subArraySum(arr, n, Sum): 
   current_sum = arr[0]
   start = 0
   
   for i in range(1, n):
       current_sum += arr[i]
       
       # when sum is greater than the given sum
       while current_sum > Sum:
           current_sum -= arr[start]
           start += 1
       
       if current_sum == Sum:
           print(start+1, i+1)
           break


import math
def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            A=list(map(int,input().split()))
            subArraySum(A, N, S)
            print()
            T-=1

if __name__ == "__main__":
    main()