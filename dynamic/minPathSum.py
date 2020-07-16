'''

Add to List

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


'''


class Solution:
    def minPathSum(self, grid):
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == 0 and y == 0:
                    continue
                elif x == 0:
                    grid[x][y] += grid[x][y-1]
                elif y == 0:
                    grid[x][y] += grid[x-1][y]
                else:
                    grid[x][y] += min(grid[x-1][y], grid[x][y-1])

        return grid[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
