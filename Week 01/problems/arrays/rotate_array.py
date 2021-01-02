# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise)
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/

# https://www.geeksforgeeks.org/array-rotation/
# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
# https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/

def reverse_(array, start, end):
	while (start < end):
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1

# Reversal Algorithm
# time is O(n) | space is O(1)
def rotate_array(array : list, d : int, n : int) -> None:
	if d == 0 or d == n: return

	# in case d is greater than n
	if d > n:
		d %= n
	reverse_(array, 0, d-1)
	reverse_(array, d, n-1)
	reverse_(array, 0, n-1)

if __name__ == '__main__':
	# inserting elements in the array
	array = list(map(int, input().strip().split()))
	n = len(array)
	d = int(input())

	rotate_array(array, d, n)
	for i in array:
		print(i, end=' ')
	print()