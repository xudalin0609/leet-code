"""
616. 安排课程
中文English
你需要去上n门九章的课才能获得offer，这些课被标号为 0 到 n-1 。
有一些课程需要“前置课程”，比如如果你要上课程0，你需要先学课程1，我们用一个匹配来表示他们： [0,1]

给你课程的总数量和一些前置课程的需求，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

样例
例1:

输入: n = 2, prerequisites = [[1,0]] 
输出: [0,1]
例2:

输入: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
输出: [0,1,2,3] or [0,2,1,3]
"""
import collections

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        indegrees = {_: 0 for _ in range(numCourses)}
        neighbors = {_: [] for _ in range(numCourses)}
        for course, pre_course in prerequisites:
            neighbors[pre_course].append(course)
            indegrees[course] += 1

        queue = collections.deque([_ for _ in indegrees if indegrees[_] == 0])
        topo_sort = []
        while queue:
            course = queue.popleft()
            topo_sort.append(course)
            for post_course in neighbors[course]:
                indegrees[post_course] -= 1
                if indegrees[post_course] == 0:
                    queue.append(post_course)
        
        if len(topo_sort) != numCourses:
            return []
        return topo_sort