class UnionFind():
    def __init__(self):
        self.parent = {}
        self.count = 0
    def find(self,p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    def add_island(self,pos):
        if pos not in self.parent:
            self.parent[pos] = pos
            self.count += 1
    def union(self,p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        print('\t', rootp, rootq)
        if rootp != rootq:
            self.parent[rootp] = self.parent[rootq]
            self.count -= 1
    def __str__(self):
        return '%s' % self.parent

class Solution:
    def numIslands2(self, m, n, positions):
        uf = UnionFind()
        ans = []
        for (r,c) in positions:
            uf.add_island((r,c))
            for neigh in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
                if neigh in uf.parent:
                    uf.union((r,c),neigh)
            ans.append(uf.count)
            print((r,c), ans, uf)
        return ans

m=3
n=3
positions=[[0,0],[0,1],[1,2],[2,1]]
s = Solution()
print(s.numIslands2(m,n, positions))
