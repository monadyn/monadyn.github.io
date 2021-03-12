# Time:  O(n)
# Space: O(h), h is height of binary tree
import collections
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    
 
class Solution(object):
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)
 
    def sumNumbersRecu(self, root, num):
        if root is None:
            return 0
 
        if root.left is None and root.right is None:
            return num * 10 + root.val
 
        return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)

#recursive
    def sumNumbers1(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res
         
    def dfs(self, root, value):
        if root:
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value*10+root.val)
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val

#bfs + stack
    def sumNumbers2(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res

#bfs + queue
    def sumNumbers3(self, root):
        if not root:
            return 0
        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            #node, value = queue.popleft()
            node, value = queue.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    queue.append((node.left, value*10+node.left.val))
                if node.right:
                    queue.append((node.right, value*10+node.right.val))
        return res
    
n5=TreeNode(5)
n1=TreeNode(1)
n9=TreeNode(9, n5, n1)
n0=TreeNode(0)

s=Solution()
r=TreeNode(4, n9, n0)
print(s.sumNumbers(r))
print(s.sumNumbers1(r))
print(s.sumNumbers2(r))
print(s.sumNumbers3(r))
