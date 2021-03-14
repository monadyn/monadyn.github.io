from pprint import pprint

t1 = [[1,1,0], [1,1,0], [0,0,1]]
t2 = [[1,1,0], [1,1,1], [0,1,1]]
for r in t1:
    print(r)


def findCircleNum(M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cnt, N = 0, len(M)
        vset = set()
        def dfs(n):
            for x in range(N):
                if M[n][x] and x not in vset:
                    vset.add(x)
                    dfs(x)


        for x in range(N):
            if x not in vset:
                cnt += 1
                dfs(x)
        return cnt
print(findCircleNum(t1))


for r in t2:
    print(r)
