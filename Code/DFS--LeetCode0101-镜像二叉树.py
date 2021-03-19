class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def checkSysmmetric(left, right):
        if None == left and None == right:
            return True
        elif None == left or None == right:
            return False
        elif left.val != right.val:
            return False
        return checkSysmmetric(left.left, right.right) and checkSysmmetric(left.right, right.left)
def isSymmetric(root):
        if None == root:
            return True
        return checkSysmmetric(root.left, root.right)

r1 = TreeNode(1)
n21 = TreeNode(2)
n22 = TreeNode(2)
r1.left = n21; r1.right = n22
n31 = TreeNode(3)
n32 =  TreeNode(4)
n33 = TreeNode(4)
n34 = TreeNode(3)
n21.left = n31; n21.right = n32
n22.left = n33; #n22.right = n34
print(isSymmetric(r1))
