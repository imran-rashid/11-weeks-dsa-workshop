# Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.
# https://www.geeksforgeeks.org/array-rotation/

# time is O(n) | space is O(1)
def reverse(array, start, end):
	while (start < end):
		array[start],array[end] = array[end],array[start]
		start += 1
		end -= 1

def rotate_array(array, d, n):
	reverse(array, 0, d-1) 
	reverse(array, d, n-1)
	reverse(array, 0, n-1)

# time is O(d*n) | space is O(1)
def array_rotation_(array, d, n):
	for i in range(d):
		temp = array[0] # store 0th value every iteration

		# shift all elements
		for j in range(n-1):
			array[j] = array[j+1]
		array[n-1] = temp

# time is O(n) | space is O(n)
def array_rotation(array, d, n):
	temp = [0]*d
	for i in range(d):
		temp[i] = array[i]

	index = 0
	for j in range(n-d):
		array[index] = array[j+d]
		index += 1

	for k in range(d):
		array[index] = temp[k]
		index += 1

if __name__ == '__main__':
	array = list(map(int, input().strip().split()))
	n = len(array)
	d = int(input())

	array_rotation_(array, d, n)
	print(array)