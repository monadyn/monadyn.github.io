import collections
def hasPath(maze, start, destination):       
        row, col = len(maze),len(maze[0])
        queue = collections.deque([(start[0],start[1])])
        visited = set()
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        def neighbors(x,y):
            temp=[]
            used = set()
            used.add((x,y))
            for dx, dy in dirs:
                nx,ny = x,y
                while 0 <= nx+dx < row and 0 <= ny+dy < col and maze[nx+dx][ny+dy] == 0:
                    nx+=dx
                    ny+=dy
                if (nx,ny) not in used:
                    temp.append((nx, ny))
            return temp
            
        while queue:
            cell = queue.popleft()
            if cell in visited: continue
            if cell == (destination[0], destination[1]): return True
            visited.add(cell)
            for neighbor in neighbors(cell[0],cell[1]):
                queue.append(neighbor)                
        return False


maze = [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]]
s = (0, 4)
e1 = (3, 2)
e2 = (4, 4)
print(hasPath(maze, s, e1))
print(hasPath(maze, s, e2))
