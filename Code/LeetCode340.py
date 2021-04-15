MAX_CHARS = 26
def isValid(count, k):
    val = 0
    for i in range(MAX_CHARS):
        if count[i] > 0:
            val += 1
    return (k >= val)
# Finds the maximum substring with exactly k unique characters
def kUniques(s, k):
    print(s)
    u = 0 # number of unique characters
    n = len(s)
    # Associative array to store the count
    count = [0] * MAX_CHARS
 
    # Tranverse the string, fills the associative array
    # count[] and count number of unique characters
    for i in range(n):
        if count[ord(s[i])-ord('a')] == 0:
            u += 1
        count[ord(s[i])-ord('a')] += 1 
    # If there are not enough unique characters, show
    # an error message.
    if u < k:
        print ("Not enough unique characters")
        return
    print(count)
    # Otherwise take a window with first element in it.
    # start and end variables.
    curr_start = 0
    curr_end = 0
 
    # Also initialize values for result longest window
    max_window_size = 1
    max_window_start = 0
 
    # Initialize associative array count[] with zero
    count = [0] * len(count)
    count[ord(s[0])-ord('a')] += 1 # put the first character
    print(count) 
    for r in range(1,n):
        count[ord(s[r])-ord('a')] += 1
        curr_end+=1
 
        # If there are more than k unique characters in
        # current window, remove from left side
        while not isValid(count, k):
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1
 
        # Update the max window size if required
        if curr_end-curr_start+1 > max_window_size:
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start
 
    print ("Max substring is : " + s[max_window_start:max_window_start  + max_window_size]
    + " with length " + str(max_window_size))
 
# Driver function
s = "aabacbebebe"
k = 3
k = 2
kUniques(s, k)
 
