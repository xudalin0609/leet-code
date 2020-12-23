"""
597. 具有最大平均数的子树
中文English
给一棵二叉树，找到有最大平均值的子树。返回子树的根结点。

样例
样例1

输入：
{1,-5,11,1,2,4,-2}
输出：11
说明:
这棵树如下所示：
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
11子树的平均值是4.333，为最大的。
样例2

输入：
{1,-5,11}
输出：11
说明:
     1
   /   \
 -5     11
1,-5,11 三棵子树的平均值分别是 2.333,-5,11。因此11才是最大的
注意事项
LintCode会打印出根结点为你返回节点的子树，保证有最大平均数子树只有一棵
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    average, node = 0, None

    def findSubtree2(self, root):
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        merge_sum, size = left_sum + right_sum + root.val, left_size + right_size + 1
        if self.node is None or merge_sum * 1.0 / size > self.average:
            self.node = root
            self.average = merge_sum * 1.0 / size
        return merge_sum, size