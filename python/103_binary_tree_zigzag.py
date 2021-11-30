# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        discovered = {}
        discovered[root] = True
        zig = False
        
        output = []
        output.append([root.val])
        
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                v = q.popleft()
                
                if v.left and v.left not in discovered:
                    q.append(v.left)
                    discovered[v.left] = True
                    level.append(v.left.val)
                    
                if v.right and v.right not in discovered:
                    q.append(v.right)
                    discovered[v.right] = True
                    level.append(v.right.val)
            
            if len(level) == 0:
                continue
            if zig:
                output.append(level)
            else:
                level.reverse()
                output.append(level)
            zig = not zig
                    
        return output