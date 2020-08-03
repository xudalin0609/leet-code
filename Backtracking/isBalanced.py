# LintCode 93
"""
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
"""

"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        return self.divideConquer(root)[0]

    def divideConquer(self, root):
        # write your code here
        if root is None:
            return True, 0

        left_is_balanced, left_height = self.divideConquer(root.left)
        right_is_balanced, right_height = self.divideConquer(root.right)
        root_height = max(left_height, right_height) + 1

        if left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1:
            return True, root_height
        return False, root_height
