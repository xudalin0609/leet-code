"""
15. 全排列
中文English
给定一个数字列表，返回其所有可能的排列。

样例
样例 1：

输入：[1]
输出：
[
  [1]
]
样例 2：

输入：[1,2,3]
输出：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
挑战
使用递归和非递归分别解决。

注意事项
你可以假设没有重复数字。
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        subsets = []
        self.dfs(nums, [], set(), subsets)
        return subsets

    def dfs(self, nums, subset, visited, subsets):
        if len(subset) == len(nums):
            subsets.append(subset.copy())
            return

        for num in nums:
            if num in visited:
                continue
            subset.append(num)
            visited.add(num)
            self.dfs(nums, subset, visited, subsets)
            visited.remove(num)
            subset.pop()
        return

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))

    class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        used = set()
        count = 0
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                left -= 1
            else:
                if nums[left] in used:
                    continue
                used.add(nums[left])
                count += 1
        
        return count
            