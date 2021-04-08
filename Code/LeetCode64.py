def minPathSum(grid):
        #动态规划： 自底而上
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        print(dp)            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp [i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                
        return dp[len(grid)-1][len(grid[0])-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
