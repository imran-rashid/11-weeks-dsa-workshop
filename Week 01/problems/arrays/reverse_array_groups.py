# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1/
# https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size-2/
# https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/

class Solution:
	# time is O(n) | space is O(1)
	def reverse_in_groups(self, arr, N, K):
		if K == 1: 
			return

		if (K >= N):
			arr.reverse()
		else:
			for i in range(0, len(arr), K):
				start = i
				# to handle case when k is not multiple of n 
				end = min(i+K-1, N-1) # since k is const

				while (start < end):
					arr[start], arr[end] = arr[end], arr[start]
					start += 1
					end -= 1

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverse_in_groups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
