# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diam = 0

        def max_dia(node,depth):

            if not node:
                return 0
            
            leftdepth = max_dia(node.left,depth)
            rightdepth = max_dia(node.right,depth)

            self.max_diam = max(self.max_diam,leftdepth+rightdepth)

            return 1+max(leftdepth,rightdepth)

        max_dia(root,0)
        return self.max_diam