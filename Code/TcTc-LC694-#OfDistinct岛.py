from pprint import pprint

class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x, y, pos, rel_pos):
            #x,y 当前位置坐标(整个图上)
            #pos 存储shape，每个岛内1相对左上角的偏移
            #rel_pos: 相对偏移
            if grid[x][y] != 1: #一定是左上角
                return
            grid[x][y] = -1 # 岛内元素
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                if 0 <= x+dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == 1:
                    new_rel_pos = (rel_pos[0] + dx, rel_pos[1] + dy)
                    pos.append(new_rel_pos)  #计算好了相对偏移，并存储!
                    dfs(x+dx, y+dy, pos, new_rel_pos)
            
        shapes = set()
        row, col = len(grid), len(grid[0])
        pprint(grid)
        print(row, col)
        for x in range(row):
            for y in range(col):
                print(grid[x][y], end=' ')
            print()
        for x in range(row):
            for y in range(col):
                print(x,y, '=',grid[x][y])
                if grid[x][y] == 1:
                    # get the shape of island
                    pos = []   #将pos列表初始化为空
                    dfs(x, y, pos, (0, 0))  #递归求得岛屿的其他部分相对于左上角的偏移量
                    print('\t', pos)
                    shapes.add(tuple(pos)) #偏移量存入pos, 将pos转化为元组放入集合中

        print(len(shapes), shapes)                    
        return len(shapes)

s = Solution()
grid = [[1,1,0,0,1],
        [1,1,1,0,1],
        [1,0,1,0,1],
        [1,1,0,1,1]]
s.numDistinctIslands(grid)
