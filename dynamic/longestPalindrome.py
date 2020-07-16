'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1: return s
        start, max_len = 0, 0
        n = len(s)
        dp = [[False] * len(s) for _ in range(n)]
        for i in range(len(s)):
            for j in range(i+1):
                if i - j < 2 and s[i] == s[j]:
                    dp[j][i] = True
                else:
                    dp[j][i] = s[i] == s[j] and dp[j + 1][i - 1]
                if i-j+1 > max_len and dp[j][i]:
                    start = j
                    max_len = i-j+1
        return s[start:start + max_len]


if __name__ == '__main__':
    print(Solution().longestPalindrome('ac'))
