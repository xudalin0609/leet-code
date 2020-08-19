# LintCode 93
"""
93. 平衡二叉树
中文English
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。 

样例
样例  1:
	输入: tree = {1,2,3}
	输出: true
	
	样例解释:
	如下，是一个平衡的二叉树。
		  1  
		 / \                
		2  3

	
样例  2:
	输入: tree = {3,9,20,#,#,15,7}
	输出: true
	
	样例解释:
	如下，是一个平衡的二叉树。
		  3  
		 / \                
		9  20                
		  /  \                
		 15   7 

	
样例  2:
	输入: tree = {1,#,2,3,4}
	输出: false
	
	样例解释:
	如下，是一个不平衡的二叉树。1的左右子树高度差2
		  1  
		   \                
		   2                
		  /  \                
		 3   4
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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.divide_conquer(root, height=0)

    def divide_conquer(self, node, height):
        if not node:
            return True

        left_subtree_height = self.divide_conquer(node.left, height+1)
        right_subtree_height = self.divide_conquer(node.right, height+1)

        if not left_is_balanced or not right_is_balanced:
            return root_height, False

        if abs(left_subtree_height - right_subtree_height) >= 2:
            return root_height, False
        return root_height, True