# LintCode 638
"""
683. 单词拆分 III
中文English
给出一个单词表和一条去掉所有空格的句子，根据给出的单词表添加空格, 返回可以构成的句子的数量, 保证构成的句子中所有的单词都可以在单词表中找到.

样例
样例1

输入：
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
输出： 3
解释：
我们可以有如下三种方式：
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
样例2

输入：
"a"
[]
输出： 0
注意事项
忽略大小写
"""


class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # max_length, lower_dict = self.initialize(dict)
        lower_dict = set([str.lower(_) for _ in dict])
        return self.memo_search(s.lower(), 0, lower_dict, {})

    def memo_search(self, s, index, lower_dict, memo):
        if len(s) == index:
            return 1
        
        if index in memo:
            return memo[index]

        memo[index] = 0
        for i in range(index, len(s)):
            if s[index: i + 1] in lower_dict:
                memo[index] += self.memo_search(s, i + 1, lower_dict, memo)

        return memo[index]

if __name__ == "__main__":
    count = Solution().wordBreak3(
        "aaaaaaaa",
        ["aaaa", "aa", "a"])
    # "Catmat",
    # ["Cat", "mat", "Ca", "tm", "at", "C", "Dog", "og", "Do"])

    print(count)
