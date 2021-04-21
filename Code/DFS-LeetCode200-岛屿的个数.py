from pprint import pprint
import collections
from collections import defaultdict

class Graph:
    def __init__(self, grid):
        self.grid = grid  # defaultdict(list)
        pprint(self.grid)
        self.parent = defaultdict(lambda : -1)
        #self.parent = defaultdict(int)
        print(self.parent)
        self.count = 0

    def find(self, x):
        if self.parent[x] == -1:
            return x
        return self.find( self.parent[x])

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set == y_set:
            print('\t',self.parent, 'x=y' )
            return
        #print('\tx=', x, x_set,'y=',y, y_set, self.parent)
        self.parent[x_set] = y_set
        print('\t', self.parent)
        self.count -= 1

    def numIslands(self):
        if  len ( self.grid ) == 0:
            return 0
        m = len(self.grid)  #row
        n = len(self.grid[0]) #col
        ##counting all 1's in matrix****
        self.count = sum(self.grid[i][j] == '1' for i in range(m) for j in range(n) )
        print(self.count)

        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '0':
                    continue
                #here we are considering matrix as 0 to (row * col) - 1
                index = i * n + j
                print(i, j, index, self.count)
                if j + 1 < n and self.grid[i][j + 1] == '1':
                    self.union(index, index + 1)

                if i + 1 < m  and self.grid[i + 1][j] == '1':
                    self.union(index, index + n)

        return self.count
class Solution:
    def numIslands(self, grid):
        g = Graph(grid) 
        return g. numIslands()


class Solution2:
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
  ["0","1","0","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(s.numIslands(grid))
