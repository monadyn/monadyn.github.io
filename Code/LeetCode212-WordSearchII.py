import collections
class Node():
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.isWord = False
        self.s = ""
        self.cnt = 0
        
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur =  self.root
        for ch in word:
            cur.cnt += 1
            cur = cur.child[ch]
            
        cur.s = word
        cur.isWord = True
    def delWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            pre = cur
            cur = cur.child.get(ch)
            if pre.cnt > 0:
                pre.cnt -= 1
            else:
                pre.child.pop(ch)
            
    def search2(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            cur = cur.child.get(ch)
            if not ch:
                return False
        return True
            
def findWords(board, words):
        #root = Trie()
        #for word in words:
        #    root.insert(word)
        wd = WordDictionary()   
        for word in words:
            wd.addWord(word)
            
        def helper(x, y, node):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or not node or board[x][y] == "#":
                return
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            temp = board[x][y]
            cur_node = node.child.get(temp)
            if cur_node:
                if cur_node.isWord:
                    print(cur_node.s)
                    res.append(cur_node.s)
                    cur_node.isWord = False
                    #root.delete(cur_node.s)
                    wd.delWord(cur_node.s)
                for i in range(4):
                    board[x][y] = "#"
                    helper(x + dx[i], y + dy[i], node.child.get(temp))
                    board[x][y] = temp
                    
        res = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                helper(x, y, wd.root)
        return res
    
        

def findWords2(board, words):
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
#board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
#words = ["oa","oaa"]
print(findWords(board, words))
print(findWords2(board, words))
