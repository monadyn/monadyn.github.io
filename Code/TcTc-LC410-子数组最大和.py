def splitArray(nums, m):
        """
本题给出一个数组nums和一个整数m,要求把数组nums分成连续的m份，找到所有分类中，子数组最大和的最小值。
显然，最简单的方法是可以使用DFS做暴力搜索，但是这样时间复杂度相当于从n-1个元素中抽取m-1个元素，为O(n^m)，会 TLE。

因为子数组本身是连续的，我们可以想到用动态规划 Dyanmic Programming 来设计解法。定义f[i][j]为把数组 nums[0,1,..,i]分成j份后最大子数组和的最小值。显然，我们会有以下公式:
f[i][j] = max(f[k][j-1],nums[k+1]+...+nums[i) for all valid k
用动态规划，从f[0][0]出发，最后返回f[n][m] 即可。时间复杂度为O(n^2*m)，并且空间复杂度为O(n*m)。

这里，介绍一种更好的算法，运用 Binary Search 。考虑到数组元素都是非负整数，所以答案也一定是整数。同时，答案一定存在于 0 到 数组元素和sum of array之间。因此，我们只需能够判断，对于任意一个整数mid，是否存在一个分类使得nums能分成m份，并且最大子数组的和不超过mid。如果能，我们下调Binary Search，如果不能，我们上调Binary Search。

        """
        def determinTrue(target):
            #判断的算法也很简单，我们用贪心算法Greedy。用tmpsum记录当前子数组的和，用count记录当前的分类数。如果当前元素num加上tmpsum不超过mid，更新tmpsum = tmpsum + num；如果超过mid，更新tmpsum = 0并更新count = count + 1。遍历完数组nums， 当count <= m，返回 True，反之返回False。
            n = len(nums)
            tmpsum, count = 0, 1
            for num in nums:
                if num > target:
                    return False
                if tmpsum + num <= target:
                    tmpsum += num
                else:
                    tmpsum = num
                    count += 1
            return count <= m

        low, high = 0, sum(nums)
        while low + 1 < high:
            mid = int(low + (high - low) /2)
            if determinTrue(mid):
                high = mid
            else:
                low = mid
        #return i if determinTrue(low, nums, m) else high
        if determinTrue(low): print('if'); return 0
        else: print('else'); return high
    
nums = [7,2,5,10,8]
m = 2
#nums = [1,2,3,4,5]

print(splitArray(nums, m))
