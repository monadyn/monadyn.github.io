def findWords(board, words):
        """
        output: ["oath","oathf","oathfi","oathfii","oathi","oathk",         "oate","eat"]
        expect: ["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"]
        """
        words = list(set(words))
        m, n = len(board), len(board[0])
        seen = [[0]*n for _ in range(m)]
        def srch(i, j, path):
            path += board[i][j]
            f = False
            for word in words:
                if path==word and path not in res: res.append(path); words.remove(path) 
                if path in word and path!=word: f = True
            if not f: return False
            
            if seen[i][j]: return False
            
            seen[i][j] = 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and not seen[x][y]:
                    if not srch(x, y, path):
                        continue
            seen[i][j] = 0
            return False
        
        res = []
        for i in range(m):
            for j in range(n):
                if not srch(i,j,''):
                    continue
        return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
print(findWords(board, words))
