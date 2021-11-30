class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 0
        have_seen = set()
        max_l = 0
        while j != len(s):
            if s[j] in have_seen:
                have_seen.remove(s[i])
                i += 1
            else:
                have_seen.add(s[j])
                j += 1
            max_l = max(max_l, j - i)

        return max_l