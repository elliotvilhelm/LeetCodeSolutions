class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(idx, path):
            if len(path) == k:
                combinations.append(path.copy())
            
            for i in range(idx, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
         
        
        combinations = []
        backtrack(1, [])
        return combinations