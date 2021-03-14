# Time:  O(n)
# Space: O(h), h is height of binary tree
 
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
 
 
class Solution(object):
    maxSum = float("-inf")
 
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxPathSumRecu(root)
        return self.maxSum

#recursive 
    def maxPathSumRecu(self, root):
        
        if root is None:
            return 0
        print('+', root.val, self.maxSum)
        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        print('-', root.val, self.maxSum)
        return root.val + max(left, right, 0)




#print([-10,9,20,null,null,15,7])
n15=TreeNode(15)
n7=TreeNode(7)
n20=TreeNode(20, n15, n7)
n9=TreeNode(9)

s=Solution()
r=TreeNode(-10, n9, n20)
print(s.maxPathSum(r))
print()
#print(s.maxPathSum(TreeNode(-10)))
