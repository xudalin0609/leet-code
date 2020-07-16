# 680

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""
class Solution:
    def checkPalindrome(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s):
        left = 0
        right = len(s)-1
        mark = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return self.checkPalindrome(s[left+1:right+1]) or self.checkPalindrome(s[left:right])
        return True

print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))