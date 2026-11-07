# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def dfs (node, depth):

            if not node:
                return 0
            
            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)

            if node.left:
                dfs(node.left, depth +1)
            if node.right:
                dfs(node.right, depth +1)
            
        dfs(root, 0)
        return result

        