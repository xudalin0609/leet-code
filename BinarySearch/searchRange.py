# 34
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""

class Solution:
    def searchRange(self, nums, target):
        self.target = target
        left = 0
        right = len(nums)-1
        mid_target = -1
        while left < right:
            mid = (left+right)<<1
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                mid_target = mid

        if mid_target == -1:
            return [-1, -1]

        lo = self.searchFirstTarget(nums[: mid_target+1])
        hi = self.searchLastTarget(nums[mid_target:])
        return [lo, mid_target+hi]
        
    def searchFirstTarget(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)>>1
            if nums[mid] <= self.target:
                right = mid
            else:
                left = mid + 1
        return left

    def searchLastTarget(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)>>1
            if nums[mid] <= self.target:
                left = mid
            else:
                right = mid - 1
        return right

