"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


class Solution:
    def __init__(self):
        nums = []

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.findMax(0, len(nums))

    def findMax(self, left, right):
        if right - left <= 1:
            return self.nums[left]
        mid = int((left + right) / 2)
        leftMax = self.findMax(left, mid)
        rightMax = self.findMax(mid, right)
        midMax = self.findCross(left, right)
        return max(leftMax, rightMax, midMax)

    def findCross(self, left, right):
        if right - left <= 1:
            return self.nums[left]
        mid = int((left + right) / 2)
        cur = self.nums[mid]
        res = cur
        for i in range(mid + 1, right):
            cur += self.nums[i]
            res = max(res, cur)
        cur = res
        for i in range(mid - 1, left - 1, -1):
            cur += self.nums[i]
            res = max(cur, res)
        return res


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
