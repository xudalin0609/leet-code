# LintCode 88 lowestCommonAncestor

"""
88. 最近公共祖先
中文English
给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。

最近公共祖先是两个节点的公共的祖先节点且具有最大深度。

样例
样例 1:

输入：{1},1,1
输出：1
解释：
 二叉树如下（只有一个节点）:
         1
 LCA(1,1) = 1
样例 2:

输入：{4,3,7,#,#,5,6},3,5
输出：4
解释：
 二叉树如下:

      4
     / \
    3   7
       / \
      5   6
			
 LCA(3, 5) = 4
注意事项
假设给出的两个节点都在树中存在
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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.divide_conquer(root, A, B)

    def divide_conquer(self, node, A, B):
        if node is None:
            return None
        
        if node.val == A.val or node.val == B.val:
            return node
        
        left_has_A_or_B = self.divide_conquer(node.left, A, B)
        right_has_A_or_B = self.divide_conquer(node.right, A, B)

        if left_has_A_or_B and right_has_A_or_B:
            return node
        if left_has_A_or_B:
            return left_has_A_or_B
        if right_has_A_or_B:
            return right_has_A_or_B
        
        return None


# {1,#,2,#,3,#,4,#,5}
