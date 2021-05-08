#[3,9,20,null,null,15,7]
#[3,9,8,4,5,2,7]
#如果一个node的column是 i，那么它的左子树column就是i - 1，右子树column就是i + 1
#    0
#[___3___]
#[_9___8_]
#[4 3 2 7]

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in range(min(cols.keys()), max(cols.keys()) + 1)] \
                   if cols else []
