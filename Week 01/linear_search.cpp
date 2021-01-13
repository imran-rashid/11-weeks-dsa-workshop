// linear search on given array

#include <bits/stdc++.h>
using namespace std;

// time is O(n) | space is O(1)
int linear_search(int array[], int n, int key){
	for (int i = 0; i < n; ++i){
		if (array[i] == key)
			return i;
	}
	return -1
}

int main(){
	int n;
	cin >> n;

	int array[n];
	for (int i = 0; i < n; ++i){
		cin >> array[i];
	}
	int key;
	cin >> key;

	cout << linear_search(array, n, key) << endl;
}