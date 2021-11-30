# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)

        discovered = {}
        discovered[root] = True
        
        output = []
        output.append([root.val])
        
        while q:
            curr_level = []
            for i in range(len(q)):
                v = q.popleft()
                # print(v)
                if v.left and v.left not in discovered:
                    q.append(v.left)
                    curr_level.append(v.left.val)
                    discovered[v.left] = True
                if v.right and v.right not in discovered:
                    q.append(v.right)
                    curr_level.append(v.right.val)
                    discovered[v.right] = True
                    
            if len(curr_level) > 0: output.append(curr_level)
            
        return output