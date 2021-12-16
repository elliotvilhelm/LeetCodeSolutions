class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        m = {'even': 0, 'odd': 0}
        for i in range(len(position)):
            if position[i] % 2 == 0:
                m['even'] += 1
            else:
                m['odd'] += 1
        
        if m['even'] > m['odd']:
            return m['odd']
        else:
            return m['even']