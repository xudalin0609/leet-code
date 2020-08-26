# LintCode 90
"""
90. k数和 II
中文English
给定n个不同的正整数，整数k（1<= k <= n）以及一个目标数字。　　　　

在这n个数里面找出K个数，使得这K个数的和等于目标数字，你需要找出所有满足要求的方案。

样例
样例 1:

输入: [1,2,3,4], k = 2, target = 5
输出:  [[1,4],[2,3]]
样例 2:

输入: [1,3,4,6], k = 3, target = 8
输出:  [[1,3,4]]	
"""

class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A:
            return []

        results = []
        A.sort()

        self.dfs(A, k, target, 0, [], results)

        return results

        
    def dfs(self, A, k, target, index, tmp, results):
        if sum(tmp) == target and k == 0:
            results.append(tmp.copy())
            return

        if k <= 0 or sum(tmp) >= target:
            return


        for i in range(index, len(A)):
            num = A[i]

            if k == 0:
                continue
            tmp.append(num)
            self.dfs(A, k - 1, target, i + 1, tmp, results)
            tmp.pop()

        return results

if __name__ == "__main__":
    print(Solution().kSumII([1, 2, 3, 4], 2, 5))
    print(Solution().kSumII([1, 3, 4, 6], 3, 8))