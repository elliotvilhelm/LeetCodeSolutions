from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        counts_list = []
        for key, value in counts.items():
            counts_list.append((key, value))
        
        counts_list = list(sorted(counts_list, key=lambda x: x[1]))
        used = set()
        mods = 0
        
        for c, f in counts_list:
            if f in used:
                while f > 0 and f in used:
                    f -= 1
                    mods += 1
                used.add(f)
            else:
                used.add(f)
                    
        return mods