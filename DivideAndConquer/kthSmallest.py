"""
902. BST中第K小的元素
中文English
给一棵二叉搜索树，写一个 KthSmallest 函数来找到其中第 K 小的元素。

样例
样例 1:

输入：{1,#,2},2
输出：2
解释：
	1
	 \
	  2
第二小的元素是2。
样例 2:

输入：{2,1,3},1
输出：1
解释：
  2
 / \
1   3
第一小的元素是1。
挑战
如果这棵 BST 经常会被修改(插入/删除操作)并且你需要很快速的找到第 K 小的元素呢？你会如何优化这个 KthSmallest 函数？

注意事项
你可以假设 k 总是有效的， 1 ≤ k ≤ 树的总节点数。
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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # use binary tree iterator
        return self.divide_conquer(root)[k-1]

    def divide_conquer(self, node):
        if node is None:
            return []

        left_subtree_values = self.divide_conquer(node.left)
        right_subtree_values = self.divide_conquer(node.right)

        results = left_subtree_values + [node.val] + right_subtree_values

        return results
