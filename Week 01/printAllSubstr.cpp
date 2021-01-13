// write a program that will print all non-empty substrings of that given string
// https://www.geeksforgeeks.org/program-print-substrings-given-string/

#include <bits/stdc++.h>

void find_all_substr(std::string str, int n){
	for(int i = 0; i < n; i++){
		for(int j = 1; j <= n-i; j++){
			// str.substr(starting_point, length)
			std::cout << str.substr(i, j) << std::endl;
		}
	}
}

int main(){
	std::string str;
	std::cin >> str;

	int length = str.length();
	find_all_substr(str, length);
	return 0;
}