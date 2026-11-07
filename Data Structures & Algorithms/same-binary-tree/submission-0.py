# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and not q:
            return False
        if q and not p:
            return False
        if not p and not q:
            return True
        
        if p and q:
            if p.val != q.val:
                return False
            else:
                pval = self.isSameTree(p.right,q.right)
                qval = self.isSameTree(p.left,q.left)
                if pval and qval:
                    return True
                else:
                    return False
        

        