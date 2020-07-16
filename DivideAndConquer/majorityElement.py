"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        left = 0
        right = len(nums)
        self.nums = nums
        return self.findMajority(left, right)

    def findMajority(self, left, right):
        if right - left <= 1:
            return self.nums[left]
        mid = (left + right) >> 1
        leftMaxNum = self.findMajority(left, mid)
        rightMaxNum = self.findMajority(mid, right)
        if leftMaxNum == rightMaxNum:
            return leftMaxNum
        leftCount = self.__numsCount(leftMaxNum, self.nums[left:right])
        rightCount = self.__numsCount(rightMaxNum, self.nums[left:right])
        if leftCount > rightCount:
            return leftMaxNum
        else:
            return rightMaxNum

    def __numsCount(self, k, nums):
        count = 0
        for i in nums:
            if i == k:
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().majorityElement([3, 3, 4]))
