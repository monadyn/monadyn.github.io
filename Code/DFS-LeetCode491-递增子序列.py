
gi = 0

def dfs(nums, index, res, path):
        #path is 候选
        global gi
        print(gi, index, res, path)
        gi += 1

        if len(path) >= 2:
            res.add(tuple(path))

        #深度dfs
        for i in range(index, len(nums)):
            print('\t', i)
            if not path or nums[i] >= path[-1]:
                dfs(nums, i + 1, res, path + [nums[i]])

def findSubsequences(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        dfs(nums, 0, res, [])
        print(res)
        return [a for a in res]
    #return map(list, res)

#nums = [4, 6, 7, 7]
nums = [4, 6, 2, 7]
print('out>>',findSubsequences(nums))
print('in >>', nums)

