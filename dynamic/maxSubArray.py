'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''


class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[-1]
        dp = nums.copy()
        for i in range(1, len(nums)):
            if dp[i] + dp[i - 1] > dp[i]:
                dp[i] = dp[i] + dp[i - 1]
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
