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
        #递归，在递归到每个节点时，
        #为了两个子树中以子树根节点为起点的最长路径和的和加上自己
        if root is None:
            return 0
        print('+', root.val, self.maxSum)
        #左右子树根节点为起点的最长路径和
        #如果子树的和为负，则取0。
        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        #用经过该节点的最长路径和更新最终结果，
        self.maxSum = max(self.maxSum, root.val + left + right)
        print('-', root.val, self.maxSum)
        #并把当前节点的值加上最大子树的路径和（或0）返回给上一层，
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
