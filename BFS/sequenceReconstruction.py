"""
605. 序列重构
中文English
判断是否序列 org 能唯一地由 seqs重构得出. org是一个由从1到n的正整数排列而成的序列，1<=n<=10^4​ 。 
重构表示组合成seqs的一个最短的父序列 (意思是，一个最短的序列使得所有 seqs里的序列都是它的子序列).
判断是否有且仅有一个能从 seqs重构出来的序列，并且这个序列是org。

样例
例1:

输入:org = [1,2,3], seqs = [[1,2],[1,3]]
输出: false
解释:
[1,2,3] 并不是唯一可以被重构出的序列，还可以重构出 [1,3,2]
例2:

输入: org = [1,2,3], seqs = [[1,2]]
输出: false
解释:
能重构出的序列只有 [1,2].
例3:

输入: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
输出: true
解释:
序列 [1,2], [1,3], 和 [2,3] 可以唯一重构出 [1,2,3].
例4:

输入:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
输出:true
"""
import collections

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        return org == self.topo_sort(graph)

    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for num in seq:
                graph[num] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
        
        return graph
    
    def topo_sort(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []
        while queue:
            if len(queue) > 1:
                return
            
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) == len(graph):
            print(topo_order, graph)
            return topo_order
        
        return

print(Solution().sequenceReconstruction([1], []))