# lintcode 587

"""
给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.

样例
例1:

输入: nums = [1,1,2,45,46,46], target = 47 
输出: 2
解释:

1 + 46 = 47
2 + 45 = 47

例2:

输入: nums = [1,1], target = 2 
输出: 1
解释:
1 + 1 = 2
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if nums is None or target is None:
            return None

        nums.sort()
        used_nums = {}
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if used_nums.get(nums[left]) is not None:
                left += 1
                continue

            if used_nums.get(nums[right]) is not None:
                right -= 1
                continue

            if nums[left] + nums[right] == target:
                count += 1
                used_nums[nums[left]] = True
                used_nums[nums[right]] = True
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        
        return count

if __name__ == "__main__":
    print(Solution().twoSum6([7,11,11,1,2,3,4], 22))