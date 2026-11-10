class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        visited = set()

        rows, cols = len(grid),len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            area = 1
            for dr,dc in directions:
                row = r + dr
                col = c + dc
                if row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col] == 1:
                    area+= dfs(row,col)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))
        
        return max_area

        