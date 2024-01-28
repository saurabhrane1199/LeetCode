# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0])]*len(grid)
        dp[0][0]=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0:
                    grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j]+grid[i][j-1])
                elif i>0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
        
        return grid[-1][-1]

        