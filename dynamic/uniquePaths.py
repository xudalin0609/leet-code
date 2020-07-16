'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

'''


class Solution:
    def uniquePaths(self, m, n):
        grid_row = [1]*n
        grid_col = [1] + [0]*(n-1)
        grid_path = [grid_row] + [grid_col]*(m-1)
        for x in range(1, m):
            for y in range(1, n):
                grid_path[x][y] = grid_path[max(0, x-1)][max(0, y)] + grid_path[max(0, x)][max(0, y-1)]
        print(grid_path)
        return grid_path[m-1][n-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(1, 1))
