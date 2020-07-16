'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[-1][-1] == 1:
            return 0
        for x in range(len(obstacleGrid)):
            if obstacleGrid[x][0] == 1:
                break
            obstacleGrid[x][0] = -1

        for x in range(len(obstacleGrid[0])):
            if obstacleGrid[0][x] == 1:
                break
            obstacleGrid[0][x] = -1

        for x in range(1, len(obstacleGrid)):
            for y in range(1, len(obstacleGrid[0])):
                if obstacleGrid[x][y] == 1:
                    continue
                obstacleGrid[x][y] = min(0, obstacleGrid[max(0, x - 1)][max(0, y)]) + min(0, obstacleGrid[max(0, x)][
                    max(0, y - 1)])

        print(obstacleGrid)

        return abs(obstacleGrid[-1][-1])


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[1, 0]]))
