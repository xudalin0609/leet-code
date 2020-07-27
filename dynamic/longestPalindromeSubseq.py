# lintcode 667
"""
给一字符串 s, 找出在 s 中的最长回文子序列的长度. 你可以假设 s 的最大长度为 1000.

您在真实的面试中是否遇到过这个题？  
样例
样例1

输入： "bbbab"
输出： 4
解释：
一个可能的最长回文序列为 "bbbb"
样例2

输入： "bbbbb"
输出： 5
"""
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if s is None:
            return None
        
        length = len(s)

        if length <= 1:
            return length
        
        dp_helper = [[0] * length for _ in range(length)]
        for right in range(length):
            dp_helper[right][right] = 1
            for left in range(right, -1, -1):
                if s[left] == s[right]:
                    dp_helper[left][right] == dp_helper[left - 1][right + 1]
                else:
                    dp_helper[left][right] == max(dp_helper[left - 1][right], dp_helper[left][right + 1])

        return dp_helper[0][length-1]
        

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 使用dp思想
        n = len(s)
        dp = [[0] * n for i in range(n)]
        if s is None:
            return None
        
        if n == 0:
            return 0

        for i in range(n):
            dp[i][i] = 1

        for left in range(n, -1, -1):
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left + 1][right],dp[left][right - 1])
        return dp[0][n-1]


if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq("bbbab"))
    print(Solution().longestPalindromeSubseq("bbbb"))
    print(Solution().longestPalindromeSubseq("b"))
    print(Solution().longestPalindromeSubseq("bv"))
    print(Solution().longestPalindromeSubseq("bb"))
    print(Solution().longestPalindromeSubseq(""))
