"""

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
"""
class Solution:
    def mySqrt(self, x):
        left = 0
        right = x
        if x == 1:
            return x
        while True:
            mid = (left+right)>>1
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid
            else:
                return mid
            if mid*mid <= x and (mid+1)*(mid+1) >x:
                return mid
        
if __name__ == "__main__":
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(2))
    print(Solution().mySqrt(3))
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(5))
    print(Solution().mySqrt(6))
    print(Solution().mySqrt(7))
    print(Solution().mySqrt(8))
    print(Solution().mySqrt(9))
