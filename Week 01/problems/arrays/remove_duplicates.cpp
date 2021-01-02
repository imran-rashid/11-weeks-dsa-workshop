// Given a sorted array, the task is to remove the duplicate elements from the array
// https://www.geeksforgeeks.org/remove-duplicates-sorted-array/
// https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/0/

#include <bits/stdc++.h>
using namespace std;

// time is O(n) | auxiliary space is O(1)
int remove_duplicates(int array[], int length){
	if (length == 0 or length == 1)
		return length;

	int index = 0;
	for(int i = 0; i < length-1; i++){
		if (array[i] != array[i+1]){
			array[index] = array[i];
			index += 1;
		}
	}
	array[index] = array[length-1];
	return index + 1;
}

int main(){
	int n;
	cin >> n;

	cin.ignore();
	int array[n];
	for(int i = 0; i < n; i++)
		cin >> array[i];

	int new_length = remove_duplicates(array, n);
	for(int i = 0; i < new_length; i++)
		cout << array[i] << " ";
	cout << endl;

	return 0;
}