class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        obstacle = {}
        obstacle[(1,3)] = obstacle[(3,1)] = 2
        obstacle[(1,7)] = obstacle[(7,1)] = 4
        obstacle[(1,9)] = obstacle[(9,1)] = 5
        obstacle[(2,8)] = obstacle[(8,2)] = 5
        obstacle[(3,7)] = obstacle[(7,3)] = 5
        obstacle[(3,9)] = obstacle[(9,3)] = 6
        obstacle[(4,6)] = obstacle[(6,4)] = 5
        obstacle[(9,7)] = obstacle[(7,9)] = 8
        
        n_comb = 0
        visited = set()
        
        def dfs(num, count, path):
            nonlocal n_comb
            nonlocal visited
            
            if m <= count <= n:
                n_comb += 1
                combinations.append(path.copy())
            
            if count == n:
                return
            
            visited.add(num)
            for i in range(1, 10):
                #if num != i and (num, i) not in obstacle or ((num,i) in obstacle and i in visited):
                if i not in visited:
                    if (num,i) in obstacle and obstacle[(num, i)] not in visited:
                        continue
                    path.append(i)
                    dfs(i, count+1, path)
                    path.pop()
            
            visited.remove(num)
                
        combinations = []
        for i in range(1, 10):
            dfs(i, 1, [i])
        
        #print(combinations)
        return n_comb