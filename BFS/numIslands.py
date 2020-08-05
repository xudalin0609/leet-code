# LintCode 433
"""

433. 岛屿的个数
中文English
给一个 01 矩阵，求不同的岛屿的个数。

0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。

样例
样例 1：

输入：
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
输出：
3
样例 2：

输入：
[
  [1,1]
]
输出：
1
"""
import collections

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def numIslands(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0

        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands
        

    def bfs(self, grid, x, y, visited):
        # queue = collections.deque([(x, y)])
        queue = [(x, y)]
        visited.add((x, y))

        while queue:
            # x, y = queue.popleft()
            x, y = queue.pop()
            for delta_x, delta_y in self.DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))


    def is_valid(self, grid, x, y, visited):
        if (0 <= x <= len(grid) - 1) and (0 <= y <= len(grid[x]) - 1) and grid[x][y] == 1 and (x, y) not in visited:
            return True
        return False

if __name__ == "__main__":
    print(Solution().numIslands([
                                    [1,1,0,0,0],
                                    [0,1,0,0,1],
                                    [0,0,0,1,1],
                                    [0,0,0,0,0],
                                    [0,0,0,0,1]
                                ]))
