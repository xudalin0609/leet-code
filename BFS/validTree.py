"""
178. 图是否是树
中文English
给出 n 个节点，标号分别从 0 到 n - 1 并且给出一个 无向 边的列表 (给出每条边的两个顶点), 写一个函数去判断这张｀无向｀图是否是一棵树

样例
样例 1:

输入: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
输出: true.
样例 2:

输入: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
输出: false.
注意事项
你可以假设我们不会给出重复的边在边的列表当中. 无向边　[0, 1] 和 [1, 0]　是同一条边， 因此他们不会同时出现在我们给你的边的列表当中。
"""
import collections
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        visited = set()
        for from_node, to_node in edges:
            neighbors[from_node].append(to_node)
            neighbors[to_node].append(from_node)
        

        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        if len(visited) == n:
            return True
        return False
            
if __name__ == "__main__":
    print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print(Solution().validTree(1, []))
    print(Solution().validTree(2, []))
    print(Solution().validTree(10, [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]]))
