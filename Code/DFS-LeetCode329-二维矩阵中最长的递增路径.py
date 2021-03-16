class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        cache = [[-1] * n for _ in range(m)]
        #使用cache保存已经访问过的位置，这样能节省了很多搜索的过程，然后有个continue是为了剪枝。
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, cache, m, n, i, j)
                res = max(res, path)
        return res
        
    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 1
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            path = 1 + self.dfs(matrix, cache, m, n, x, y)
            res = max(path, res)
        cache[i][j] = res
        return cache[i][j]

s = Solution()
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(s.longestIncreasingPath(nums))
#时间复杂度是O((MN)^2)，空间复杂度是O(MN)。
