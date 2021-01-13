// Given a number n, find the sum of first natural numbers
// https://www.geeksforgeeks.org/program-find-sum-first-n-natural-numbers/

#include <iostream>
using namespace std;

// Efficient Solution O(1) | O(1) [avoid overflow error]
int sum(int n){
    if (n & 1){ // when n is odd
        return n * ((n+1)/2);
    }
    return (n/2) * (n+1);
}

// time and space is O(n) | O(1) respectively 
int sum2(int n){
    int total = 0;
    
    for(int i = 1; i <= n; i++){
        total += i;
    }
    return total;
}

// with formula [this program causes overflow, even if the result is not beyond integer limit]
int sum3(int n){
    return (n*(n+1)) / 2;
}

int main(){
    int number;
    cout << "Enter the number: ";
    cin >> number;

    cout << "sum is " << sum(number) << endl;
    cout << "sum is " << sum2(number) << endl;
    cout << "sum is " << sum3(number) << endl;
}