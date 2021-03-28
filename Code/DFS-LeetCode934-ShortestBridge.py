import collections
class Solution:

    def shortestBridge(self, A) -> int:
        st = collections.deque() #[]
        M = len(A)
        N = len(A[0])
        visited = [[0] * N for _ in range(M)]
        
        #find an island by DFS
        def dfs(A, i, j):
            if visited[i][j]: return
            visited[i][j] = 1
            A[i][j] = 2
            st.append((i,j))
             
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x = i+dx
                y = j+dy
                #if x<len(A) and x>-1 and y<len(A[0]) and y>-1 and A[i][j] == 1:
                if x<len(A) and x>-1 and y<len(A[0]) and y>-1 and A[x][y] == 1:
                    dfs(A, x, y)
            
        flag = True
        for i in range(len(A)):
            if not flag: break
            for j in range(len(A[0])):
                if A[i][j] == 1 and flag == True:
                    flag = False
                    dfs(A, i, j)
                    break
       
        print('st=', st)
        #bfs flip 0->1 until 1
        def bfs(A, i, j):
            #if visited[i][j]: return
            #visited[i][j] = 1
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x = i+dx
                y = j+dy
                #if x<len(A) and x>-1 and y<len(A[0]) and y>-1 and A[i][j] == 1:
                if x<len(A) and x>-1 and y<len(A[0]) and y>-1 and A[x][y] == 1:
                     return True

                if x<len(A) and x>-1 and y<len(A[0]) and y>-1 and A[x][y] == 0: #and (x,y) not in st:
                    print(x, y)
                    st.append((x, y))
            return False
        
        n = 0
        while len(st) > 0:
            size = len(st)
            while size > 0:
                i, j = st.popleft()
                if bfs(A, i, j):
                    return n
                size -= 1
            n += 1
        return -1


s = Solution()
A = [[0,1],[1,0]]
print(s.shortestBridge(A))
