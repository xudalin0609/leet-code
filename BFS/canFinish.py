"""
615. 课程表
中文English
现在你总共有 n 门课需要选，记为 0 到 n - 1.
一些课程在修之前需要先修另外的一些课程，比如要学习课程 0 你需要先学习课程 1 ，表示为[0,1]
给定n门课以及他们的先决条件，判断是否可能完成所有课程？

样例
例1:

输入: n = 2, prerequisites = [[1,0]] 
输出: true
例2:

输入: n = 2, prerequisites = [[1,0],[0,1]] 
输出: false
"""
import collections
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        n = numCourses
        node_neighour = {x : [] for x in range(n)}
        node_indegree = {x : 0 for x in range(n)}
        
        for from_node, to_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighour[from_node].append(to_node)
        
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = collections.deque(start_nodes)
        result = []

        while queue :
            node = queue.popleft()
            result.append(node)
            for neighbor in node_neighour[node] :
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0 :
                    queue.append(neighbor)
        return len(result) == numCourses
        
if __name__ == "__main__":
    # print(Solution().canFinish(1, []))
    # print(Solution().canFinish(2, [[1,0]]))
    print(Solution().canFinish(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]))