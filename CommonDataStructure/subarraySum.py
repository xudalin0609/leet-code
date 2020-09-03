# LintCode 138
"""
138. 子数组之和
中文English
给定一个整数数组，找到和为 0 的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置

样例
样例 1:

输入: [-3, 1, 2, -3, 4]
输出: [0,2] 或 [1,3]	
样例解释： 返回任意一段和为0的区间即可。
样例 2:

输入: [-3, 1, -4, 2, -3, 4]
输出: [1,5]
注意事项
至少有一个子数组的和为 0
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_sum = 0
        prefix_hash = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum in prefix_hash:
                return [prefix_hash[prefix_sum] + 1, i]

            prefix_hash[prefix_sum] = i

        return -1, -1

if __name__ == "__main__":
    print(Solution().subarraySum([-3, 1, 3, -3, 4]))
    # print(Solution().subarraySum([_ for _ in range(1, 10)]))
