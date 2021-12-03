class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])        
        for i in nums:
            subsets_len = len(subsets)
            for j in range(subsets_len):
                s = subsets[j].copy()
                s.append(i)
                subsets.append(s)
                
        return subsets