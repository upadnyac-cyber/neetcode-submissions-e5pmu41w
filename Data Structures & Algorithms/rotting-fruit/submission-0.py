class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row,col = len(grid),len(grid[0])
        fresh = 0
        time = 0
        q = collections.deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    n_r,n_c = r+dr,c+dc
                    if n_r in range(row) and n_c in range(col) and grid[n_r][n_c] == 1:
                        q.append((n_r,n_c))
                        grid[n_r][n_c] = 2
                        fresh-=1
            time+=1
        
        return time if fresh == 0 else -1





        