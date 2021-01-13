# write a program that will print all non-empty substrings of that given string
# https://www.geeksforgeeks.org/program-print-substrings-given-string/

def find_all_substr(string : str, length : int):
	for i in range(0, length):
		for j in range(i+1, length+1): # length+1 cause for grave last index
			print(string[i:j])

if __name__ == '__main__':
	string = input()
	length = len(string)
	
	find_all_substr(string, length)