# Given a sorted array containing only 0s and 1s, find the transition point. Transition point is where 0 ends and 1 begins
# https://www.geeksforgeeks.org/find-transition-point-binary-array/
# https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1/

# time is O(logn) | Space is O(1)
def transitionPoint(arr, n):
    lower_bound = 0
    upper_bound = n-1
    
    while (lower_bound <= upper_bound):
        mid = (lower_bound + upper_bound) // 2

        if (arr[mid] == 0):
            lower_bound = mid + 1
        
        elif arr[mid] == 1:
            if (mid == 0 or (arr[mid - 1] == 0)):
                return mid
            
            upper_bound = mid - 1
                
    return -1

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
