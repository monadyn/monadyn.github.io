class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
import collections
def distanceK(root, target, K):
        """
        :type root: TreeNode, 根节点
        :type target: TreeNode， 目标节点
        :type K: int, 距离
        :rtype: List[int]
        """
        def build_graph(node,par):
            if not node:
                return
            if node.left:
                graph[node].append(node.left)
            if node.right:
                graph[node].append(node.right)
            if par:
                graph[node].append(par)
            build_graph(node.left,node)
            build_graph(node.right,node)
        graph = collections.defaultdict(list) #k: node, v： list
        build_graph(root,None)
        print(graph)

        ans = []
        q = collections.deque()
        q.append((target,0))
        visited = set()
        visited.add(target.val)
        while q:
            node,dis = q.popleft() #FIFO, BFS
            if dis == K:
                ans.append(node.val)
            for nei in graph[node]:
                if nei.val not in visited:
                    q.append((nei,dis+1))
                    visited.add(nei.val)
        return ans

#树转化为图通常的表达方式，也就是字典；再从target节点出发，BFS寻找特定距离的点
n0= TreeNode(0)
n1= TreeNode(1)
n2= TreeNode(2)
n3= TreeNode(3)
n4= TreeNode(4)
n5= TreeNode(5)
n6= TreeNode(6)
n7= TreeNode(7)
n8= TreeNode(8)
n2.left = n7; n2.right=n4
n5.left = n6; n5.right=n2
n1.left = n0; n1.right=n8
n3.left = n5; n3.right=n1

print(distanceK(n3, n5, 2))
