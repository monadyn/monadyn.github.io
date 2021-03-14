from pprint import pprint

t1 = [['X', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X']]

pprint(t1)

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.

#从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。
#而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。

    def solve(self, board):
        def dfs(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y]!='O':return

            board[x][y] = 'D'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        if len(board) == 0: return
        m = len(board); n = len(board[0])

        #外围
        #没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变
        for i in range(m):
            dfs(i, 0); dfs(i, n-1)
        for j in range(1, n-1):
            dfs(0, j); dfs(m-1, j)

        #然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] == 'X'
                elif board[i][j] == 'D': board[i][j] == 'O'
 
s = Solution()
s.solve(t1)

pprint(t1)
