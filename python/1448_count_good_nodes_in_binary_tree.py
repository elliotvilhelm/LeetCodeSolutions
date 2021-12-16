# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes = 0
        def dfs(node, curr_max):
            nonlocal good_nodes
            if not node:
                return
            
            if node.val >= curr_max:
                good_nodes += 1
                curr_max = node.val
            
            if node.left:
                dfs(node.left, curr_max)
            
            if node.right:
                dfs(node.right, curr_max)
                
        dfs(root, float("-inf"))
        return good_nodes