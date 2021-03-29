from pprint import pprint

class Solution(object):
    def maxAreaOfIsland(self, grid):
        if len(grid) == 0: return 0
        N, M = len(grid), len(grid[0])
        vsted = [[0]*M for _ in range(N)]
        
        def dfs(i, j, n):
            if vsted[i][j] == 1: return
            vsted[i][j] = 1
            n += 1
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = i+dx,j+dy
                if -1<x<N and -1<y<M and grid[x][y] == 1 and vsted[i][j] == 0:
                    dfs(x,y, n)
                    
        res = 0
        for i in range(N):
            for j in range(M):
                n = 0
                if grid[i][j] == 1 and vsted[i][j] == 0:
                    dfs(i, j, n)
                    res = max(res, n)
        return res

    def maxAreaOfIsland2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i <= row - 1 and 0 <= j <= col - 1 and grid[i][j]:
                grid[i][j] = 0 # 重要，防止再次搜索
                return  1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0
        return max(dfs(i, j) for i in range(row) for j in range(col))

    def maxAreaOfIsland1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        self.island = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    self.res = max(self.res, self.island)
                    self.island = 0
        return self.res
    
    def dfs(self, grid, i, j): # ensure grid[i][j] == 1
        M, N = len(grid), len(grid[0])
        grid[i][j] = 0
        self.island += 1
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < M and 0 <= y < N and grid[x][y]:
                self.dfs(grid, x, y)
s = Solution()

t1 =[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
t1 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

t2 = [[0,0,0,0,0,0,0,0]]

pprint(t1)
print(s.maxAreaOfIsland2(t1))
#print(s.maxAreaOfIsland(t1))
#print(t2)
