# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def get_sum(node):
            nonlocal total_tilt
            if not node:
                return 0
            
            left = get_sum(node.left)
            right = get_sum(node.right)
            tilt = abs(left-right)
            total_tilt += tilt
            return left + right + node.val
        
        total_tilt = 0
        get_sum(root)
        return total_tilt