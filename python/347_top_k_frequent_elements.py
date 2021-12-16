class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else: 
                counts[i] = 1
        l = []
        for key,val in counts.items():
            l.append((key,val))
        
        l = sorted(l, key=lambda x: x[1], reverse=True)
        l = list(map(lambda x: x[0], l[:k]))
        return l