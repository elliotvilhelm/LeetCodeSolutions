# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        def getPaths(node, remaining,  path):
            print(path)
            if not node:
                return
            
            remaining -= node.val
            if remaining == 0 and not node.right and not node.left:
                path.append(node.val)
                combinations.append(list(path))
                path.pop()
                return
            else:
                
                path.append(node.val)
                left = getPaths(node.left, remaining, path)
                if len(path) > 0: path.pop()
                
                path.append(node.val)
                right = getPaths(node.right, remaining, path)
                if len(path) > 0: path.pop()
                return
         
        combinations = []
        getPaths(root, targetSum, [])
        return combinations