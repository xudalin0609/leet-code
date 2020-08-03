# LintCode 480
"""

480. 二叉树的所有路径
中文English
给一棵二叉树，找出从根节点到叶子节点的所有路径。

样例
样例 1:

输入：{1,2,3,#,5}
输出：["1->2->5","1->3"]
解释：
   1
 /   \
2     3
 \
  5
样例 2:

输入：{1,2}
输出：["1->2"]
解释：
   1
 /   
2     
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        left_tree_paths = self.binaryTreePaths(root.left)
        right_tree_paths = self.binaryTreePaths(root.right)
        paths = []
        for path in left_tree_paths + right_tree_paths:
            paths.append(str(root.val) + '->' + path)

        return paths

    def templateBinaryTrees(self, root):
        if root is None:
            return "res"

        left_tree_results = self.templateBinaryTrees(root.left)
        right_tree_results = self.templateBinaryTrees(root.right)
        tree_results = left_tree_results + right_tree_results
        return tree_results