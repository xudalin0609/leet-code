"""
11. 二叉查找树中搜索区间
中文English
给定一个二叉查找树和范围[k1, k2]。按照升序返回给定范围内的节点值。

样例
样例 1:

输入：{5},6,10
输出：[]
        5
它将被序列化为 {5}
没有数字介于6和10之间
样例 2:

输入：{20,8,22,4,12},10,22
输出：[12,20,22]
解释：
        20
       /  \
      8   22
     / \
    4   12
它将被序列化为 {20,8,22,4,12}
[12,20,22]介于10和22之间
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        res = self.__helper(root, k1, k2, [])
        res.sort()
        return res

    def __helper(self, node, k1, k2, range_list):
        if node is None:
            return range_list
        self.__helper(node.left, k1, k2, range_list)
        self.__helper(node.right, k1, k2, range_list)
        if node.val >= k1 and node.val <= k2:
            range_list.append(node.val)

        return range_list

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        result = []
        self.travel(root, k1, k2, result)
        return result
    
    def travel(self, root, k1, k2, result):
        if root is None:
            return
    	# 剪枝，如果当前节点小于等于k1，不必访问左子树
        if root.val > k1:
            self.travel(root.left, k1, k2, result)
            
        if k1 <= root.val and root.val <= k2:
            result.append(root.val)
        # 剪枝，如果当前节点大于等于k2，不必访问右子树
        if root.val < k2:
            self.travel(root.right, k1, k2, result)