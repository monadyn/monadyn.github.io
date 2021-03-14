class Solution:
    def findWords(self, board, words):
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)
        
        #构建trie， prefix tree
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                #print(cur, trie)
                cur = cur.setdefault(letter, {})
                print('\t', letter,  trie)
            print(word, trie)
            cur['#'] = word
        print(trie)
        #DFS，使用Trie进行剪枝，一个优化是，把找到的单词对应的字典树的节点也删掉

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    print(i, j, board[i][j], 'dfs')
                    dfs(i, j, trie)
        return res


words = ["oath","pea","eat","rain"]
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
from pprint import pprint
pprint(board)
s=Solution()
print(s.findWords(board, words))
