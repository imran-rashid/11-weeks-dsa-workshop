# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.
# https://practice.geeksforgeeks.org/problems/find-immediate-smaller-than-x/0/

# time is O(n) | space is O(1)
def immediateSmaller(arr, n, x):
	smallest = -1

	for i in arr:
		if (i > smallest and i < x):
			smallest = i

	if smallest != -1:
		return smallest
	return -1
	
if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        
        ans=immediateSmaller(arr,n,x)
        print(ans)
# } Driver Code Ends