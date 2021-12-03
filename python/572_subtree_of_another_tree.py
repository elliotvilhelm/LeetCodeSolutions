# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        elif root.val == subRoot.val and self.checkSubtree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)     
    
    def checkSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot: # one is null
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)