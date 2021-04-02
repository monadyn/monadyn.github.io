import collections
from heapq import heappop, heappush
def countRestrictedPaths(n, edges):
        #先求出每个节点的distanceToLastNode作为节点值，用Dijkstra。
        #此时问题转化为找所有满足路径上节点值单调减的路径：找所有=>DFS。
        #并且从任意一点开始的路径数一旦确定，它的值就可以cached以复用=>cached DFS。
        d, g = [float('inf')] * (n + 1), collections.defaultdict(list)
        for i, (a, b, w) in enumerate(edges):
            g[a].append((b, w))
            g[b].append((a, w))
        d[n] = 0
        heap = [(d[n], n)]
        while heap:
            dis, cur = heappop(heap)
            for nei, w in g[cur]:
                cand = dis + w
                if cand < d[nei]:
                    d[nei] = cand
                    heappush(heap, (d[nei], nei))
        res, M, visited = [0], 10 ** 9 + 7, [-1] * (n + 1)

        def dfs(cur, g, e, res):
            if visited[cur] != -1:
                return visited[cur]
            visited[cur] = 0
            if cur == e:
                visited[cur] = 1
                return visited[cur]
            for nei, _ in g[cur]:
                if d[nei] <= d[cur]:
                    continue
                visited[cur] = (visited[cur] % M + dfs(nei, g, e, res) % M) % M
            return visited[cur]
        return dfs(n, g, 1, res)
 
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(countRestrictedPaths(n, edges))
