# LintCode 109
"""
109. 数字三角形
中文English
给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

样例
样例 1

输入下列数字三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
输出： 11
解释： 从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
样例 2

输入下列数字三角形：
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
输出： 12
解释： 从顶到底部的最小路径和为12 ( 2 + 2 + 7 + 1 = 12)。
注意事项
如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。
"""


# dfs althorithm, time complexity fall short
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return None

        if len(triangle[0]) == 0:
            return 0

        return min(self.dfs(triangle, 0, 0, triangle[0][0], []))

    def dfs(self, triangle, x, y, path_sum, results):
        print(x, y)

        if x == len(triangle) - 1:
            results.append(path_sum)
            return results

        for delta_y in [0, 1]:
            x_ = x + 1
            y_ = y + delta_y
            if not self.is_arrived(triangle, x_, y_):
                continue

            self.dfs(triangle, x_, y_, path_sum + triangle[x_][y_], results)
        return results

    def is_arrived(self, triangle, x_, y_):
        if x_ >= len(triangle):
            return False
        if 0 > y_ or y_ >= len(triangle[x_]):
            return False

        return True


# divide and conquer, use memory search
class Solution:

    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})
        
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]
        
        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]




if __name__ == "__main__":
    print(Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))

    # print(Solution().minimumTotal(
    #     [
    #         [2],
    #         [3, 2],
    #         [6, 5, 7],
    #         [4, 4, 8, 1]
    #     ]
    # ))

    # print(Solution().minimumTotal(
    #     [[-10]]
    # ))
