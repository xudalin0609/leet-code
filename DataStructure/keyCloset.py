"""
612. K个最近的点
中文English
给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。

样例
例1:

输入: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 
输出: [[1,1],[2,5],[4,4]]
例2:

输入: points = [[0,0],[0,9]], origin = [3, 1], k = 1
输出: [[0,0]]
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def get_distance(self, a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2

    def kClosest(self, points, origin, k):
        self.heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        ret = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))
        ret.reverse()
        return ret
