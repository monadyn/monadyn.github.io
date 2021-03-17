# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == root2:
            print('\t', root1, root2)
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False

        print(root1.val, root2.val)
        #A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
        #some number of flip operations 可以flip，也可以不flip
        return (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right)) or \
                (flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))

#root1 = [0,null,1]; root2 = [0,1]
r1 = TreeNode(0)
r2 = TreeNode(0)
n11 = TreeNode(1)
n21 = TreeNode(1)
r1.right = n11
r2.left = n21
print(flipEquiv(r1, r2))
