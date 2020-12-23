# LintCode 192
"""
192. 通配符匹配
中文English
判断两个可能包含通配符“？”和“*”的字符串是否匹配。匹配规则如下：

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个串完全匹配才算匹配成功。

样例
样例1

输入:
"aa"
"a"
输出: false
输出2

输入:
"aa"
"aa"
输出: true
输出3

输入:
"aaa"
"aa"
输出: false
输出4

输入:
"aa"
"*"
输出: true
说明: '*' 可以替换任何字符串
输出5

输入:
"aa"
"a*"
输出: true
样例6

输入:
"ab"
"?*"
输出: true
说明: '?' -> 'a' '*' -> 'b'
样例7

输入:
"aab"
"c*a*b"
输出: false
注意事项
1<=|s|, |p| <= 1000
s仅包含小写英文字母
p包含小写英文字母，？和 *
"""


"""
class Solution:
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})
        
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
            
        # source is empty
        if len(source) == i:
            # every character should be "*"
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True
            
        if len(pattern) == j:
            return False
            
        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:                
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
        
        
    def is_match_char(self, s, p):
        return s == p or p == '?'
"""


class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})

    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(source) == i:
            for index in range(j, len(pattern)):
                if pattern[index] != "*":
                    return False
            return True

        if len(pattern) == j:
            return False

        if pattern[j] != "*":
            match = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:
            match = self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 1, memo)

        memo[(i, j)] = match

        return match

    # def is_match_helper(self, source, i, pattern, j, memo):
    #     if (i, j) in memo:
    #         return memo[(i, j)]

    #     # source is empty
    #     if len(source) == i:
    #         # every character should be "*"
    #         for index in range(j, len(pattern)):
    #             if pattern[index] != '*':
    #                 return False
    #         return True

    #     if len(pattern) == j:
    #         return False

    #     if pattern[j] != '*':
    #         matched = self.is_match_char(source[i], pattern[j]) and \
    #             self.is_match_helper(source, i + 1, pattern, j + 1, memo)
    #     else:
    #         matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
    #             self.is_match_helper(source, i, pattern, j + 1, memo)

    #     memo[(i, j)] = matched
    #     return matched

    def is_match_char(self, s, p):
        return s == p or p == '?'


if __name__ == "__main__":
    print(Solution().isMatch("aa", "aa"))
