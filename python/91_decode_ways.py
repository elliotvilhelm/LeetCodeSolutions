class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return self.getDecodings(0, s)
    
    @lru_cache(maxsize=None)
    def getDecodings(self, index: int, s: str) -> int:
        if index == len(s): # made it to the end
            return 1
        elif s[index] == '0':
            return 0
        
        result = self.getDecodings(index + 1, s)
        if int(s[index:index+2]) <= 26 and index + 2 <= len(s):
            result += self.getDecodings(index + 2, s)
        
        return result