# Given a sorted array, the task is to remove the duplicate elements from the array
# https://www.geeksforgeeks.org/remove-duplicates-sorted-array/
# https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/0/

# time is O(n) | auxiliary space is O(1)
def remove_duplicates(array : list, length : int) -> int:
	if length == 0 or length == 1: # there is no need to interchange
		return length

	index = 0
	for i in range(0, length-1):
		if array[i] != array[i+1]:
			array[index] = array[i] # ith value will copy to new index
			index += 1

	# when only one element to check it will directly copy the element
	array[index] = array[length-1]
	return index + 1 # since index was started from 0

if __name__ == '__main__':
	array = list(map(int, input().split()))
	length = len(array)

	new_array_length = remove_duplicates(array, length)
	# print(array) [after interchange it will print original array]

	# but we want only unique values 
	for i in range(0, new_array_length):
		print(array[i], end=' ')
	print()
