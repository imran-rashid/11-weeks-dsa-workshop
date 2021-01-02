// Given an unsorted array arr[] of size N, rotate it by D elements (clockwise)
// https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/

/**
* https://www.geeksforgeeks.org/array-rotation/
* https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/ (method 4)
* https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/
*/

#include <bits/stdc++.h>
using namespace std;

// time is O(n) | space is O(1)
void rotateArr(int arr[], int d, int n){
	if (d == 0 or d == n){
		return;
	}

	// in case d is greater
	if (d > n){
		d %= n;
	}
    reverse(arr, arr+d);
    reverse(arr+d, arr+n);
    reverse(arr, arr+n);
}

int main() {
	int t;
	//taking testcases
	cin >> t;
	
	while(t--){
	    int n, d;
	    
	    //input n and d
	    cin >> n >> d;
	    
	    int arr[n];
	    //inserting elements in the array
	    for(int i = 0; i < n; i++){
	        cin >> arr[i];
	    }
	    
	    //calling rotateArr() function
	    rotateArr(arr, d,n);
	    
	    //printing the elements of the array
	    for(int i =0;i<n;i++){
	        cout << arr[i] << " ";
	    }
	    cout << endl;
	}
	return 0;
}