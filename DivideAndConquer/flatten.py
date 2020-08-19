# LintCode 453
"""

453. 将二叉树拆成链表
中文English
将一棵二叉树按照前序遍历拆解成为一个 假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。

样例
样例 1：

输入：{1,2,5,3,4,#,6}
输出：{1,#,2,#,3,#,4,#,5,#,6}
解释：
     1
    / \
   2   5
  / \   \
 3   4   6
 
1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
样例 2：

输入：{1}
输出：{1}
解释：
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
    def flatten(self, root):
        self.flatten_and_return_last_node(root)
        
    # restructure and return last node in preorder
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None
            
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)
        
        # connect 
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        return right_last or left_last or root


class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            node.left = None
            
            if stack:
                node.right = stack[-1]
            else:
                node.right = None