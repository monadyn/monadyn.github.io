from pprint import pprint
import collections

def findMinDiff(arr, n): 
    # Initialize difference as infinite 
    diff = 10**20
      
    # Find the min diff by comparing difference 
    # of all possible pairs in given array 
    for i in range(n-1): 
        for j in range(i+1,n): 
            if abs(arr[i]-arr[j]) < diff: 
                diff = abs(arr[i] - arr[j]) 
  
    # Return min diff 
    return diff, i, j 
  
# Driver code 
arr = [1, 5, 3, 19, 18, 25] 
n = len(arr) 
print("Minimum difference is ", findMinDiff(arr, n))
