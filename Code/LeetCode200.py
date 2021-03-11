from pprint import pprint
import collections

class Solution:
    def isSafe(self, grid, row, col, visited):
        return( 0<= row < len(grid) and
               0 <= col < len(grid[0]) and
               grid[row][col] == "1" and visited[row][col] == False)

    def dfs(self, row, col, visited, grid):
        valid_row = [-1, 0, 0, 1]
        valid_col = [0, -1, 1, 0]
        visited[row][col] = True
        for neighbour in range(len(valid_row)):
            new_row = row + valid_row[neighbour]
            new_col = col + valid_col[neighbour]
            if(self.isSafe(grid, new_row, new_col, visited)):
                self.dfs(new_row, new_col, visited, grid)



    def numIslands(self, grid):
        visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]
        pprint(visited)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row, col, grid[row][col], visited[row][col])
                if(grid[row][col] == "1" and visited[row][col] == False):
                    self.dfs(row, col, visited, grid)
                    count += 1
        pprint(visited)
        return count


s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(s.numIslands(grid))
