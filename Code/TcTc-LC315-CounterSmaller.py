class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n

    def lowbit(self, x):
        return x & -x

    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

def countSmaller(nums):
        dic = {}
        for i, num in enumerate(sorted(list(set(nums)))):
            print(i, num)
            dic[num] = i + 1
        print(nums)
        print(dic)
        tree = FenwickTree(len(nums))
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = tree.sum(dic[nums[i]] - 1)
            tree.add(dic[nums[i]], 1)
        return ans

def countSmaller2(nums):
        def sort(enum):
            print(enum)
            half = len(enum) // 2
            print('\t', half)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            print('\t', enum, smaller)
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
nums = [5,2,3, 6,1]
print(countSmaller(nums))
