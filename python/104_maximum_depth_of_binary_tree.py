# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_max(root, 0)
        
    def get_max(self, node, h):
        if not node:
            return h
        else:
            return max(self.get_max(node.left, h+1), self.get_max(node.right, h+1))