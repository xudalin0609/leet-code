# LintCode 154
"""
154. 正则表达式匹配
中文English
实现支持'.'和'*'的正则表达式匹配。

'.'匹配任意一个字母。

'*'匹配零个或者多个前面的元素。

匹配应该覆盖整个输入字符串，而不仅仅是一部分。

需要实现的函数是：bool isMatch(string s, string p)

isMatch("aa","a") → false

isMatch("aa","aa") → true

isMatch("aaa","aa") → false

isMatch("aa", "a*") → true

isMatch("aa", ".*") → true

isMatch("ab", ".*") → true

isMatch("aab", "c*a*b") → true

样例
样例 1:

输入："aa"，"a"
输出：false
解释：
无法匹配
样例 2:

输入："aa"，"a*"
输出：true
解释：
'*' 可以重复 a
"""


class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here
        return self.is_match_helper(s, len(s) - 1, p, len(p) - 1, {})

    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            for index in range(i):
                if source[index] != "*":
                    return False
            return True

        if j == 0:
            return False

        if pattern[j] != "*":
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i - 1, pattern, j - 1, memo)
        else:
            matched = self.is_match_helper(source, i - 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j - 1, memo)

        memo[(i, j)] = matched
        return matched

    def is_match_char(self, s, p):
        return s == p or p == "."


class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})

    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True

    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # source is empty
        if len(source) == i:
            return self.is_empty(pattern[j:])

        if len(pattern) == j:
            return False

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 2, memo)
        else:
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)

        memo[(i, j)] = matched
        return matched

    def is_match_char(self, s, p):
        return s == p or p == '.'

    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False

        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True


if __name__ == "__main__":
    print(Solution().isMatch("aa", "aa"))
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("abab", "a*b*"))
