# Binary search on array

# time is O(logn) | space is O(1)
def binary_search(array, key):
	start = 0
	last = len(array) - 1 # it's catch up the last index which is n-1
	while (start <= last):
		mid = (start+last) // 2
		if array[mid] == key:
			return mid
		if array[mid] < key:
			start = mid + 1
		else:
			last = mid - 1
	return -1

if __name__ == '__main__':
	array = [2,5,6,10,15]
	key = 15
	print(binary_search(array, key))