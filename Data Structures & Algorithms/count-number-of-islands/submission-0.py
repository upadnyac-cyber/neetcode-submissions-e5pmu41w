class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        g_row,g_col = len(grid),len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):

            if (r,c) in visited:
                return
            
            visited.add((r,c))
            for dr,dc in directions:
                rows = r+dr
                cols = c+dc
                if rows in range(g_row) and cols in range(g_col) and (rows,cols) not in visited and grid[rows][cols] == "1":
                    dfs(rows,cols)


        for r in range(g_row):
            for c in range(g_col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1
        
        return islands
        