def uniquePathsWithObstacles(obstacleGrid):
        #space complexity: O(m*n) -> O(1)
        print(obstacleGrid)
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        #初始化状态
        f = False
        for i in range(N):
            if obstacleGrid[i][0] == 1 or f == True:
                obstacleGrid[i][0] = 0
                f = True
            else:
                obstacleGrid[i][0] = 1
        print(obstacleGrid)
        f = False
        for j in range(1, M):
            print(j, f)
            if obstacleGrid[0][j] == 1 or f == True:
                obstacleGrid[0][j] = 0
                f = True
            else:
                obstacleGrid[0][j] = 1
        print(obstacleGrid)
        #from bottom to top
        for i in range(1,N):
            for j in range(1,M):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[N-1][M-1]
grid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(grid)) 
