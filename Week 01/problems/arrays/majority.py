# Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y. If both elements have the same frequency, then return the smaller element.
# https://practice.geeksforgeeks.org/problems/who-has-the-majority/1/

# time is O(n) | space is O(1)
def majorityWins(arr, n, x, y):
	x_count = y_count = 0

	for i, value in enumerate(arr):
		if x == value:
			x_count += 1
		elif y == value:
			y_count += 1

	if x_count == y_count:
		return min(x, y)
	elif x_count > y_count:
		return x
	else:
		return y

if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(majorityWins(arr,n,x,y))
        T-=1
