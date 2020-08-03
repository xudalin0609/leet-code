"""
457. 经典二分查找问题
中文English
在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回 -1。

样例
样例 1：

输入：nums = [1,2,2,4,5,5], target = 2
输出：1 或者 2
样例 2：

输入：nums = [1,2,2,4,5,5], target = 6
输出：-1
挑战
O(logn) 的时间

"""

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or target is None:
            return None

        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid 
        
        if nums[right] == target:
            return right
        
        return -1

if __name__ == "__main__":
    print(Solution().findPosition([0], 2)) # -1
    print(Solution().findPosition([], 2)) # -1
    print(Solution().findPosition([0, 1], 2)) # -1
    print(Solution().findPosition([0, 1, 2], 2))
    print(Solution().findPosition([0, 0 ,1], 2))
    print(Solution().findPosition([1,2,2,4,5,5], 2))
    print(Solution().findPosition([1,2,2,4,5], 5))
    print(Solution().findPosition([1,1,1], -2))