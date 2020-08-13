# LintCode 900
"""
900. 二叉搜索树中最接近的值
中文English
给一棵非空二叉搜索树以及一个target值，找到在BST中最接近给定值的节点值

样例
样例1

输入: root = {5,4,9,2,#,8,10} and target = 6.124780
输出: 5
解释：
二叉树 {5,4,9,2,#,8,10}，表示如下的树结构：
        5
       / \
     4    9
    /    / \
   2    8  10
样例2

输入: root = {3,2,4,1} and target = 4.142857
输出: 4
解释：
二叉树 {3,2,4,1}，表示如下的树结构：
     3
    / \
  2    4
 /
1
注意事项
给出的目标值为浮点数
我们可以保证只有唯一一个最接近给定值的节点
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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here

        closest_value = root.val

        left_value = self.find_closest_val(root.left, target, closest_value)
        right_value = self.find_closest_val(root.right, target, closest_value)

        return self.get_closer_val(left_value, right_value, target)
    
    def find_closest_val(self, node, target, closest_value):

        if node is None:
            return closest_value


        left_value = self.find_closest_val(node.left, target, closest_value)
        right_value = self.find_closest_val(node.right, target, closest_value)

        if self.get_closer_val(left_value, right_value, target) == left_value:
            closest_value = self.get_closer_val(left_value, closest_value, target)
        else:
            closest_value = self.get_closer_val(right_value, closest_value, target)

        return closest_value
    
    def get_closer_val(self, val1, val2, target):
        if abs(val1 - target) > abs(val2 - target):
            return val2
        return val1


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    

    """
    def closestValue(self, root, target):
        if root is None:
            return(9999999999)
            
        leftcloset = self.closestValue(root.left, target) 
        
        rightcloset = self.closestValue(root.right, target)
        
        
        root_diff = abs(root.val - target)
        leftdiff = abs(leftcloset -target ) 
        rightdiff = abs(rightcloset -target ) 
        if root_diff == min(root_diff,leftdiff, rightdiff):
            return root.val
        elif leftdiff == min(root_diff, leftdiff, rightdiff):
            return leftcloset
        else:
            return rightcloset