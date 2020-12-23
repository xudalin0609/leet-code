"""

18. 子集 II
中文English
给定一个可能具有重复数字的列表，返回其所有可能的子集。

样例
样例 1：

输入：[0]
输出：
[
  [],
  [0]
]
样例 2：

输入：[1,2,2]
输出：
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
挑战
你可以同时用递归与非递归的方式解决么？

注意事项
子集中的每个元素都是非降序的
两个子集间的顺序是无关紧要的
解集中不能包含重复子集
"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        subsets = []
        nums.sort()
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, start, subset, subsets):
        subsets.append(subset.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            # print(subset)
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
        
        
print(Solution().subsetsWithDup([1 , 1, 1]))