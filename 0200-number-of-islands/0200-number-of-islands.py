class Solution:
    def __init__(self):
        self.count=0
        
    def coloring(self, grid, i, j):
        if i+1<len(grid) and grid[i+1][j]=='1':
            grid[i+1][j]='0'
            self.coloring(grid, i+1, j)
            
        if i-1>=0 and grid[i-1][j]=='1':
            grid[i-1][j]='0'
            self.coloring(grid, i-1, j)

        if j+1<len(grid[i]) and grid[i][j+1]=='1':
            grid[i][j+1]='0'
            self.coloring(grid, i, j+1)

        if j-1>=0 and grid[i][j-1]=='1':
            grid[i][j-1]='0'
            self.coloring(grid, i, j-1)
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    grid[i][j]='0'
                    self.count+=1
                    self.coloring(grid, i, j)
        return self.count
                    
                    

        