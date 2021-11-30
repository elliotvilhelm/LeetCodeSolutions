class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if there is a match then lcs(text1[1:], text2[2:]) + 1
        # else max(lcs(text1[1:], text2), lcs(text1, text2[1:]))
        @lru_cache(maxsize=None)
        def lcs(t1: str, t2: str) -> int:
            if len(t1) == 0 or len(t2) == 0:
                return 0
            if t1[0] == t2[0]:
                return lcs(t1[1:], t2[1:]) + 1
            else:
                return max(lcs(t1[1:], t2), lcs(t1, t2[1:]))
        
        return lcs(text1, text2)