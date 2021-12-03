class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining: int, index: int, path: List[int]):
            if remaining == 0:
                combinations.append(list(path))
                return
            elif remaining < 0:
                return
            
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path)
                path.pop()
        
        combinations = []
        backtrack(target, 0, [])
        return combinations