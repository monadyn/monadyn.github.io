from pprint import pprint
def findCircleNum(M):
        def dfs(M, curr, n):
            print('in', curr)
            for i in range(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(M, i, n)
            print('out', curr)

        n = len(M)
        ans = 0
        for i in range(n):
            if M[i][i] == 1:
                ans += 1
                dfs(M, i, n)

        return ans
t1 = [[1,1,0], [1,1,0], [0,0,1]]
t1 = [[1,0,1], [0,1,0], [1,0,1]]
t2 = [[1,1,0], [1,1,1], [0,1,1]]
for r in t1:
    print(r)
print(findCircleNum(t1))
#for r in t2:
#    print(r)
