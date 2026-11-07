# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res = True

        def findBalance(node):

            if not node:
                return 0
            
            leftDepth = findBalance(node.left)
            rightDepth = findBalance(node.right)

            if self.res and abs(leftDepth - rightDepth) <= 1:
                self.res = True
            else:
                self.res = False
            
            return 1 + max(leftDepth,rightDepth)
        
        findBalance(root)

        return self.res