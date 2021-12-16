class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            result += s[0]
        return result