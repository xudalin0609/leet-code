"""
86. 二叉查找树迭代器
中文English
设计实现一个带有下列属性的二叉查找树的迭代器：
next()返回BST中下一个最小的元素

元素按照递增的顺序被访问（比如中序遍历）
next()和hasNext()的询问操作要求均摊时间复杂度是O(1)
样例
样例 1:

输入：{10,1,11,#,6,#,12}
输出：[1, 6, 10, 11, 12]
解释：
二叉查找树如下 :
  10
  /\
 1 11
  \  \
   6  12
可以返回二叉查找树的中序遍历 [1, 6, 10, 11, 12]
样例 2:

输入：{2,1,3}
输出：[1,2,3]
解释：
二叉查找树如下 :
  2
 / \
1   3
可以返回二叉查找树的中序遍历 [1,2,3]
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""



class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        
        return node


class BSTIterator2:

    def __init__(self):
        self.stack = []
        self.findMostLeft(root)

    def findMostLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return bool(self.stack)

    def next(self):
        node = self.stack.pop()
        if node.right:
            self.findMostLeft(node.right)
        return node
