# LintCode 272
"""
272. 爬楼梯 II
中文English
一个小孩爬一个 n 层台阶的楼梯。他可以每次跳 1 步， 2 步 或者 3 步。实现一个方法来统计总共有多少种不同的方式爬到最顶层的台阶。

样例
Example 1:

Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Example 2:

Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
说明
对于n=0，我们认为答案是1。
"""
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n == 0:
            return 1
        
        return self.dfs(n, {1: 1, 2: 2, 3: 4})

    
    def dfs(self, n, cache):

        if n in cache:
            return cache[n]

        if n < 0:
            return 0
        
        count = sum([self.dfs(n - _ - 1, cache) for _ in range(3)])
        cache[n] = count

        return count


if __name__ == "__main__":
    print(Solution().climbStairs2(4))