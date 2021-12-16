class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(maxsize=None)
        def backtrack(index: int, s: str, wordSet: FrozenSet[str]):
            if index == len(s):
                return True
            
            for end in range(index + 1, len(s) + 1):
                prefix = s[index:end]
                if prefix in wordSet and backtrack(end, s, wordSet):
                    return True
            return False
        
        return backtrack(0, s, frozenset(wordDict))