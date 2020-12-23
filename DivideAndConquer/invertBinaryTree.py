"""
175. 翻转二叉树
中文English
翻转一棵二叉树。左右子树交换。

样例
样例 1:

输入: {1,3,#}
输出: {1,#,3}
解释:
	  1    1
	 /  =>  \
	3        3
样例 2:

输入: {1,2,3,#,#,4}
输出: {1,3,2,#,4}
解释: 
	
      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4
挑战
递归固然可行，能否写个非递归的？
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root.left is None or root.right is None:
            root.left, root.right = root.right, root.left
            return root
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        return root

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)

    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)
        
        return root
    
    def dfs(self,root):
        if root is None:
            return
        
        left = root.left
        right = root.right
        root.left = right
        root.right = left