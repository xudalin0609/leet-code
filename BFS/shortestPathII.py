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
    def is_valid(self, node, grid):
        if node[0] > len(grid[0]):
            return False
        if node[1] < len(grid):
            return False
        if grid[node[1]][grid[0]] == 1:
            return False
        return True

    def shortestPath(self, grid, source, destination):
        queue = collections.deque([source])
        distance = {source: 0}
        while queue:
            node = queue.popleft()
            if node == destination:
                break
            for x_delta, y_detlta in self.DIRECTIONS:
                next_location = [node[0] + x_delta, node[1] + y_detlta]
                if next_location in distance:
                    continue
                if self.is_valid(next_location, grid):
                    distance[next_location] = distance[node] + 1
                    queue.append(next_location)
                
        return distance[destination]


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