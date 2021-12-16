"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            nonlocal first, last
            
            if not node:
                return
            
            helper(node.left)
            
            if not last:
                first = node
            else:
                last.right = node
                node.left = last
            
            last = node
            
            helper(node.right)
                
         
        if not root:
            return None
        
        last = None
        first = None
        helper(root)
        first.left = last
        last.right = first
        return first