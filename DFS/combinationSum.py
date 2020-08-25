# LintCode 135
"""
35. 数字组合
中文English
给定一个候选数字的集合 candidates 和一个目标值 target. 找到 candidates 中所有的和为 target 的组合.

在同一个组合中, candidates 中的某个数字不限次数地出现.

样例
样例 1:

输入: candidates = [2, 3, 6, 7], target = 7
输出: [[7], [2, 2, 3]]
样例 2:

输入: candidates = [1], target = 3
输出: [[1, 1, 1]]
注意事项
所有数值 (包括 target ) 都是正整数.
返回的每一个组合内的数字必须是非降序的.
返回的所有组合之间可以是任意顺序.
解集不能包含重复的组合.
"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []
        
        # candidates.sort()
        combinations = []
        candidates = sorted(list(set(candidates)))
        self.dfs(candidates, target, 0, [], combinations)
        return combinations


    def dfs(self, candidates, target, index, combination, combinations):
        if target < 0:
            return

        if target == 0:
            combinations.append(combination.copy())
            return

        for i in range(index, len(candidates)):
            candidate = candidates[i]
            if target < candidate:
                break

            combination.append(candidate)
            self.dfs(candidates, target - candidate, i, combination, combinations)
            combination.pop()

if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7], 7))