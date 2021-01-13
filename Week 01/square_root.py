# Given an integer x, find it’s square root. If x is not a perfect square, then return floor(√x)
# https://www.geeksforgeeks.org/square-root-of-an-integer/
# https://www.geeksforgeeks.org/square-root-of-a-perfect-square/

# time is O(logn) | space is O(1)
def square_root(number : int):
	# base case
	if number == 0 or number == 1:
		return number

	root = -1
	start = 1 # 1 to n
	end = number

	while (start <= end):
		mid = (start+end)//2
		square = mid*mid;

		# when num is perfect square
		if (square == number):
			return mid

		# when square is less than num simply store mid value
		if (square < number):
			start = mid + 1
			root = mid
		else:
			end = mid - 1

	return root

# O(√n) | O(1)
def squareRoot(num):
    if num == 0 and num == 1: 
    	return num
    
    i = 1
    square = 1
    while (square <= num):
        i += 1
        square = i*i
    
    return i-1

if __name__ == '__main__':
	num = int(input())
	print(f'square root of {num} is {square_root(num)}')