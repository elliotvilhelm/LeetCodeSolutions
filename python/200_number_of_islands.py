class Solution:
    def dfs(self, grid, i, j):
        r = len(grid) - 1
        c = len(grid[0]) - 1
        
        if i > r or j > c:
            return
        else:
            grid[i][j] = '0'
            if i+1 <= r and grid[i+1][j] == '1':
                self.dfs(grid, i+1, j)
            if j+1 <= c and grid[i][j+1] == '1':
                self.dfs(grid, i, j+1)
            if i-1 >= 0 and grid[i-1][j] == '1':
                self.dfs(grid, i-1, j)
            if j-1 >= 0 and grid[i][j-1] == '1':
                self.dfs(grid, i, j-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    total_islands += 1
         
        return total_islands