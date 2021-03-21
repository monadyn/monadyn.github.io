def sortedSquares(nums):
        l = len(nums)
        left, right = 0, l - 1
        res = [0] * l
        cur = l - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[cur] = nums[left] ** 2
                left += 1
            else:
                res[cur] = nums[right] ** 2
                right -= 1
            cur -= 1
        return res

print(sortedSquares([-7,-3,2,3,11]))
