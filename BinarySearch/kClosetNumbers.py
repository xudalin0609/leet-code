# LintCode 460
"""

460. 在排序数组中找最接近的K个数
中文English
给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。

样例
样例 1:

输入: A = [1, 2, 3], target = 2, k = 3
输出: [2, 1, 3]
样例 2:

输入: A = [1, 4, 6, 8], target = 3, k = 3
输出: [4, 1, 6]
挑战
O(logn + k) 的时间复杂度

注意事项
k是一个非负整数，并且总是小于已排序数组的长度。
给定数组的长度是正整数, 不会超过 10^410
​4
​​ 
数组中元素的绝对值不会超过 10^410
​4
​​
"""
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if A is None or target is None or k is None:
            return None

        if len(A) == 0 or k == 0:
            return []
        
        closest_num_position = self.findClosestNumber(A, target)
        res = [A[closest_num_position]]
        k -= 1
        left, right = closest_num_position-1, closest_num_position + 1
        while k > 0 and (left > 0 or right < len(A)):
            pos, left_move, right_move = self.closerNumber(A, target, left, right)
            res.append(A[pos])
            left += left_move
            right += right_move
            k -= 1
        
        return res

    def findClosestNumber(self, A, target):
        left, right = 0, len(A) - 1
        while left < right - 1:
            mid = (left + right) >> 1
            if A[mid] > target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                return mid
        
        if A[right] == target:
            return right

        return self.closerNumber(A, target, left, right)[0]
    
    def closerNumber(self, A, target, pos1, pos2):
        if pos1 < 0:
            return pos2, 0, 1
        if pos2 > len(A) - 1:
            return pos1, -1, 0

        if abs(A[pos1] - target) <= abs(A[pos2] - target):
            return pos1, -1, 0
        else:
            return pos2, 0, 1

if __name__ == "__main__":
    print(Solution().kClosestNumbers([1, 2, 3], 2, 3))
    print(Solution().kClosestNumbers([1, 4, 6, 8], 3, 3))
    print(Solution().kClosestNumbers([1,2,4,5,6,7,8,10], 5, 0))