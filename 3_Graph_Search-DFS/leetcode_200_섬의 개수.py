class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 - land
        # 0 - water

        def dfs(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            
            if grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1

        return cnt