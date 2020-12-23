"""
17. 子集
中文English
给定一个含不同整数的集合，返回其所有的子集。

样例
样例 1：

输入：[0]
输出：
[
  [],
  [0]
]
样例 2：

输入：[1,2,3]
输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
挑战
你可以同时用递归与非递归的方式解决么？

注意事项
子集中的元素排列必须是非降序的，解集必须不包含重复的子集。
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        subsets = []
        nums.sort()
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, start, subset, subsets):
        subsets.append(subset.copy())
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()

if __name__ == "__main__":
    print(Solution().subsets([1]))