"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_set = set()
        
        while p:
            p_set.add(p)
            p = p.parent
        
        while q not in p_set:
            q = q.parent
        
        return q