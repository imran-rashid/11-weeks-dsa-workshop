// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining
// https://www.geeksforgeeks.org/trapping-rain-water/

#include <bits/stdc++.h>
using namespace std;

// max from left sidebar
int left_max(int array[], int i){
	int maximum = 0;
	for(int j = 0; j <= i; j++){
		maximum = max(maximum, array[j]);
	}
	return maximum;
}

// max from right sidebar
int right_max(int array[], int i, int n){
	int maximum = 0;
	for(int j = i; j < n; j++){
		maximum = max(maximum, array[j]);
	}
	return maximum;
}

// time is O(n*n) | space is O(1)
int find_total_water(int array[], int n){
	int total_warer = 0;

	for(int i = 1; i < n-1; i++){ // 0th and n-1 index is boundary
		
		int left = left_max(array, i);
		int right = right_max(array, i, n);
		total_warer += ((min(right, left)) - array[i]);
	}
	return total_warer;
}

int main(){
	int n;
	cin >> n;

	cin.ignore();
	int array[n];
	for(int i = 0; i < n; i++){
		cin >> array[i];
	}

	int max_water = find_total_water(array, n);
	cout << "Maximum water that can be accumulated is " << max_water << " litre" << endl;
}