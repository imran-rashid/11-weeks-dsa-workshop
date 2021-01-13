# count the number of frequency in an sorted array

def frequency_count(array, length, key, flag=None):
	low = 0
	high = length - 1
	result = -1

	while (low <= high):
		mid = (low + high) // 2

		if array[mid] == key:
			result = mid

			if flag:
				# towards left (lower indices)
				high = mid - 1
			else:
				# towards right (upper indices)
				low = mid + 1
		elif array[mid] < key:
			low = mid + 1
		else:
			high = mid - 1

	return result

if __name__ == '__main__':
	array = [1,2,3,3,3,3,4,5]
	length = len(array)
	key = 3

	first_index = frequency_count(array, length, key, True)
	last_index = frequency_count(array, length, key)

	if first_index == -1:
		print(f'{key} presents 0 times')
	else:
		print(f'{key} presents {last_index - first_index + 1} times')