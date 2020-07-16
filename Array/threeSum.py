"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""
import itertools


class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        i = 0
        while i <= len(nums) - 3:
            left, right = i + 1, len(nums) - 1
            need = nums[i]
            while right - left >= 1:
                if nums[left] + nums[right] + need > 0:
                    right -= 1
                elif nums[left] + nums[right] + need < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], need])
                    left += 1
                    while right - left >= 1 and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
            while i <= len(nums) - 3 and nums[i - 1] == nums[i]:
                i += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1]))
