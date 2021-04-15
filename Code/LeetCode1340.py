def maxJumps(arr, d):
        #base
        dp = [1]*len(arr)
        seen = [0]*len(arr)
        def get_dp(i):
            if seen[i] == 1: return dp[i]
            nei_dp = []
            for nei in range(i-d, i):
                if 0<=nei<len(arr) and arr[nei]<arr[i] and max(arr[nei:i])<arr[i]:
                    nei_dp.append(get_dp(nei))
            for nei in range(i+1, i+d+1):
                if 0<=nei<len(arr) and arr[nei]<arr[i] and max(arr[i+1:nei+1])<arr[i]:
                    nei_dp.append(get_dp(nei))
                    
            if len(nei_dp)>0:
                dp[i] = max(nei_dp)+1
            seen[i] = 1
            return dp[i]
            
        #遍历所有点，求dp[i]
        for i in range(len(arr)):
            get_dp(i)
        return max(dp)
def maxJumps_err(arr, d):
        #base
        dp = [1]*len(arr)
        #遍历所有点，求dp[i]
        for i in range(len(arr)):
            print(i)
            nei_dp = []
            for nei in range(i-d, i):
                if 0<=nei<len(arr) and arr[nei]<arr[i] and max(arr[nei:i])<arr[i]:
                    nei_dp.append(dp[nei])
            for nei in range(i+1, i+d+1):
                if 0<=nei<len(arr) and arr[nei]<arr[i] and max(arr[i+1:nei+1])<arr[i]:
                    nei_dp.append(dp[nei])
                    
            if len(nei_dp)>0:
                dp[i] = max(nei_dp)+1
            print('\t', dp)
        return max(dp)

arr = [6,4,14,6,8,13,9,7,10,6,12]; d = 2
arr = [7,6,5,4,3,2,1]; d = 1
print(maxJumps(arr, d))
