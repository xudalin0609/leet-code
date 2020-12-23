"""
431. 找无向图的连通块
中文English
找出无向图中所有的连通块。

图中的每个节点包含一个label属性和一个邻接点的列表。

（一个无向图的连通块是一个子图，其中任意两个顶点通过路径相连，且不与整个图中的其它顶点相连。）

你需要返回 label 集合的列表.

样例
样例 1:

输入: {1,2,4#2,1,4#3,5#4,1,2#5,3}
输出: [[1,2,4],[3,5]]
解释: 

  1------2  3
   \     |  | 
    \    |  |
     \   |  |
      \  |  |
        4   5
样例 2:

输入: {1,2#2,1}
输出: [[1,2]]
解释:

  1--2

说明
关于图的表示

注意事项
每个连通块内部应该按照label属性升序排序. 不同的连通块之间可以是任意顺序.
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

import collections

class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        queue = collections.deque()
        visited = set()
        