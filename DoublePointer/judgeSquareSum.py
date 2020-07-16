# 633
"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False
"""

class Solution:
    def judgeSquareSum(self, c):
        import math
        left = 0
        right = int(math.sqrt(c+1))
        while left <= right:
            res = left*left+right*right
            if res > c: right -= 1
            elif res < c: left += 1
            else: return True

        return False

print(Solution().judgeSquareSum(5))