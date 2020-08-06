# LintCode 611
"""
611. 骑士的最短路线
中文English
给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空 1 表示有障碍物)，找到到达 终点 的最短路线，返回路线的长度。如果骑士不能到达则返回 -1 。

样例
例1:

输入:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
输出: 2
解释:
[2,0]->[0,1]->[2,2]
例2:

输入:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
输出:-1
说明
如果骑士的位置为 (x,y)，他下一步可以到达以下这些位置:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import collections

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    DIRECTIONS = [
        (-2, -1), (-2, 1), (-1, 2), (1, 2),
        (2, 1), (2, -1), (1, -2), (-1, -2),
    ]

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1

        quque = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}
        vistited = set()

        while quque:
            x, y = quque.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)] + 1
            for delta_x, delta_y in self.DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y) or (next_x, next_y) in distance:
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                quque.append((next_x, next_y))
        return -1

    def is_valid(self, grid, x, y):
        grid_height = len(grid) - 1
        grid_weigth = len(grid[0]) - 1
        if x < 0 or x > grid_height or y < 0 or y > grid_weigth:
            return False
        if grid[x][y] == 1:
            return False
        return True


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