def subarraySum(nums, k):
        #sum(i,j)=sum(0,j)-sum(0,i), 
        #sum(i,j) represents the sum of all the elements from index i to j-1.
        res = 0
        tb = {} #key is sum, value is count
        tb[0] = 1 #关键
        sum = 0
        for i in range(len(nums)):
            print(i)
            sum += nums[i]
            if (sum - k) in tb.keys():
                res += tb[sum - k]
            tb[sum] = 1 if sum not in tb.keys() else tb[sum] + 1
            print('\ttb', tb)
            print('\tres=', res)
        return res
nums = [1,1,1,0,2,-2]; k = 2
print(subarraySum(nums, k))
print(nums)
