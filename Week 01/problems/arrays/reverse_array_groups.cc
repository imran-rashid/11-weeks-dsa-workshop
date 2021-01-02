#include <bits/stdc++.h>
using namespace std;

class Solution{
	public:
	    void reverseInGroups(vector<long long>& arr, int n, int k){
	        if (k == 1) return;
	        if (k >= n){
	        	reverse(arr.begin(), arr.end());
	        }
	        else {
	        	for(int i = 0; i < n; i += k){
	            int start = i;
	            int end = min(i+k-1, n-1);
	            
		            while (start < end){
		                swap(arr[start], arr[end]);
		                start++;
		                end--;
		            }
	        	}
	        }
	    }
};

int main() {
    int t; 
    cin >> t; 
    while(t--){ 
        int n;
        cin >> n; 
        vector<long long> arr; 
        int k;
        cin >> k; 

        for(long long i = 0; i<n; i++)
        {
            long long x;
            cin >> x; 
            arr.push_back(x); 
        }
        Solution ob;
        ob.reverseInGroups(arr, n, k);
        
        for(long long i = 0; i<n; i++){
            cout << arr[i] << " "; 
        }
        cout << endl;
    }
}
