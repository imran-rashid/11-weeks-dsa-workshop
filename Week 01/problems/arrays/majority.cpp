// Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y. If both elements have the same frequency, then return the smaller element.
// https://practice.geeksforgeeks.org/problems/who-has-the-majority/1/

// time is O(n) | space is O(1)
int majorityWins(int arr[], int n, int x,int y){
    int x_count = 0;
    int y_count = 0;

    for (int i = 0; i < n; i++){
		if (x == arr[i]){
			x_count++;
		} else if (y == arr[i]){
			y_count += 1;
		}
	}
	
	if (x_count == y_count){
		return min(x,y);
	} else if (x_count > y_count){
		return x;
	} else {
		return y;
	}
}

int main() {
    
    int t; //Testcases
    cin>>t; // Input the testcases
    while(t--) //Until all testcases are exhausted
    {
        int n; //Size of array
        cin>>n; //Input the size
        int arr[n]; //Declaring array of size n
        for(int i=0;i<n;i++) // Running a loop to input all elements of arr
        cin>>arr[i];
        
        int x,y; //declare x and y
        cin>>x>>y; // input x and y
        cout << majorityWins(arr,n,x,y) << endl; //calling the function that you complete
    }
    
	return 0;
}