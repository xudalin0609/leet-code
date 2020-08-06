# LintCode 137
"""

137. 克隆图
中文English
克隆一张无向图. 无向图的每个节点包含一个 label 和一个列表 neighbors. 保证每个节点的 label 互不相同.

你的程序需要返回一个经过深度拷贝的新图. 新图和原图具有同样的结构, 并且对新图的任何改动不会对原图造成任何影响.

样例
样例1

输入:
{1,2,4#2,1,4#4,1,2}
输出: 
{1,2,4#2,1,4#4,1,2}
解释:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
说明
关于无向图的表示: http://www.lintcode.com/help/graph/

注意事项
你需要返回与给定节点具有相同 label 的那个节点.
"""
from collections import deque
import copy

class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node

        root = node
        nodes = self.findNodes(node)
        node_map = {}
        for node in nodes:
            node_map[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            for neighbor in node.neighbors:
                node_map[node].neighbors.append(node_map[neighbor])

        return node_map[root]
        


    def findNodes(self, node):
        queue = deque([node])
        nodes = set([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in nodes:
                    nodes.add(neighbor)
                    queue.append(neighbor)
        
        return nodes

