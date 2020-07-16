"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution:
    def threeSumClosest(self, nums, target):
        i = 0
        nums.sort()
        mark = sum(nums[:3])
        while i <= len(nums) - 3:
            left, right = i + 1, len(nums) - 1
            last = (nums[left] + nums[right] + nums[i] - target)
            while right - left >= 1:

                if nums[left] + nums[right] + nums[i] - target > 0:
                    if abs((nums[left] + nums[right] + nums[i] - target)) < abs(last):
                        last = nums[left] + nums[right] + nums[i] - target
                    right -= 1
                elif nums[left] + nums[right] + nums[i] - target < 0:
                    if abs((nums[left] + nums[right] + nums[i] - target)) < abs(last):
                        last = nums[left] + nums[right] + nums[i] - target

                    left += 1
                else:
                    return target

            if abs(last) < abs(mark - target):
                mark = last + target
            i += 1
        return mark


if __name__ == "__main__":
    print(Solution().threeSumClosest([0,2,1,-3], 1))
