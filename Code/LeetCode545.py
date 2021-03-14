# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def leftBoundary(node):
            if not node or (node.left is None and node.right is None):
                return 
            b.append(node.val)
            if node.left:
                leftBoundary(node.left)
            else:
                leftBoundary(node.right)
            
        def leaves(node):
            if not node:
                return
            leaves(node.left)
            if node != root and node.left is None and node.right is None:
                b.append(node.val)
            
            leaves(node.right)
            
        def rightBoundary(node):
            if not node or (node.left is None and node.right is None):
                return            
            if node.right:
                rightBoundary(node.right)
            else:
                rightBoundary(node.left)
            b.append(node.val)
            
        
        # base case
        if not root: return []
        b = [root.val]
        #DFS. 分别定义三个函数, 实现查找左边界, 叶子, 右边界.
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return b

r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r5 = TreeNode(5)
r6 = TreeNode(6)
r7 = TreeNode(7)
r8 = TreeNode(8)
r9 = TreeNode(9)
r10 = TreeNode(10)

r1.left = r2
r1.right = r3

r2.left = r4
r2.right = r5

r3.left = r6

r4.left = r7
r4.right = r8

r5.left = r9
r6.left = r10

s = Solution()
print(s.boundaryOfBinaryTree(r1))


