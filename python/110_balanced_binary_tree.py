# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        root_balance = abs(self.get_height(root.left) - self.get_height(root.right)) <= 1
        left_balance = True
        right_balance = True
        if root.left:
            left_balance = self.isBalanced(root.left)
        if root.right:
            right_balance = self.isBalanced(root.right)
            
        return root_balance and left_balance and right_balance
        
    def get_height(self, node):
        if not node:
            return -1
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1