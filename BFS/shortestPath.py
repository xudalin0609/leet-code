# LintCode 611
"""
中文English
在一个 n * m 的棋盘中(二维矩阵中 0 表示空 1 表示有障碍物)，骑士的初始位置是 (0, 0) ，他想要达到 (n - 1, m - 1) 这个位置，骑士只能从左边走到右边。找出骑士到目标位置所需要走的最短路径并返回其长度，如果骑士无法达到则返回 -1.

样例
例1:

输入:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
输出:
3
解释:
[0,0]->[2,1]->[0,2]->[2,3]
例2:

输入:
[[0,1,0],[0,0,1],[0,0,0]]
输出:
-1
说明
如果骑士所在位置为(x,y)，那么他的下一步可以到达以下位置:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
"""
import collections

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath2(self, grid):
            # write your code here
            if not grid or grid[-1][-1] == 1:
                return -1
                
            n = len(grid)
            m = len(grid[0])
    
            delta = [(1,2), (-1,2), (2,1), (-2,1)]
            queue = [(0,0)]
            step = 0
            while queue:
                size = len(queue)
                step += 1
                for i in range(size):
                    x, y = queue.pop()
                    for delta_x, delta_y in delta:
                        if x + delta_x == n - 1 and y + delta_y == m - 1:
                            return step
                        if n > x + delta_x >= 0 and m > y + delta_y >= 0 and grid[x + delta_x][y + delta_y] != 1:
                            grid[x + delta_x][y + delta_y] = 1
                            queue.insert(0, (x+delta_x, y+delta_y))
            return -1

if __name__ == "__main__":
    print(Solution().shortestPath([[0,0,0],
                                   [0,0,0],
                                   [0,0,0]],
                                   [2, 0],
                                   [2, 2]
                                ))
    print(Solution().shortestPath([[0,1,0],
                                   [0,0,1],
                                   [0,0,0]],
                                   [2, 0],
                                   [2, 2]
                                ))