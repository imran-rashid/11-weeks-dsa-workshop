# Given an array arr[] of size N, find the first repeating element. The element should occurs more than once and the index of its first occurrence should be the smallest.
# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/0/
# https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

# time is O(n) | space is O(1)
def first_repeating_element(array, length):
	index = -1
	my_dict = {}

	# traverse array from right to left
	for i in range(length-1, -1, -1):
		# when ele visiting more than once
		if array[i] in my_dict.keys():
			index = i
		else:
			my_dict[array[i]] = 1

		if index != -1:
			return index
	return -1

if __name__=='__main__':
    t=int(input())
    
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(first_repeating_element(arr, n))