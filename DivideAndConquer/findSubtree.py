# LintCode 596
"""

596. 最小子树
中文English
给一棵二叉树, 找到和为最小的子树, 返回其根节点。输入输出数据范围都在int内。

样例
样例 1:

输入:
{1,-5,2,1,2,-4,-5}
输出:1
说明
这棵树如下所示：
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
整颗树的和是最小的，所以返回根节点1.
样例 2:

输入:
{1}
输出:1
说明:
这棵树如下所示：
   1
这棵树只有整体这一个子树，所以返回1.
注意事项
LintCode会打印根节点为你返回节点的子树。保证只有一棵和最小的子树并且给出的二叉树不是一棵空树。
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        if root is None:
            return root

        minimum, node, sum_root= self.helper(root)

        return node

    def helper(self, root):
        if root is None:
            return float('inf'), None, 0

        left_minimum, left_node, left_sum = self.helper(root.left)
        right_minimum, right_node, right_sum = self.helper(root.right)

        sum_root = left_sum + root.val + right_sum

        if left_minimum == min(left_minimum, right_minimum, sum_root):
            return left_minimum, left_node, sum_root
        if right_minimum == min(left_minimum, right_minimum, sum_root):
            return right_minimum, right_node, sum_root

        return sum_root, root, sum_root
