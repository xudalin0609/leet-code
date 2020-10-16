# LintCode 638
"""
582. 单词拆分II
中文English
给一字串s和单词的字典dict,在字串中增加空格来构建一个句子，并且所有单词都来自字典。
返回所有有可能的句子。

样例
样例 1:

输入："lintcode"，["de","ding","co","code","lint"]
输出：["lint code", "lint co de"]
解释：
插入一个空格是"lint code"，插入两个空格是 "lint co de"
样例 2:

输入："a"，[]
输出：[]
解释：字典为空

"""


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return []
        # return self.dfs(s, wordDict, 0, "", [])
        return self.memory_search(s, wordDict, {})

    # dfs解法，时间复杂度最后的case过不去

    def dfs(self, s, wordDict, start_index, substring, result):
        if s == substring.replace(" ", ""):
            result.append(substring[1:])
            return result

        for word in wordDict:
            word_length = len(word)
            if len(word) == 0:
                continue
            if word == s[start_index: start_index + word_length]:
                self.dfs(s, wordDict, start_index + word_length,
                         substring + " " + word, result)
        return result

    def memory_search(self, s, dictWord, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in dictWord:
                continue
            sub_partitions = self.memory_search(s[i:], dictWord, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)

        if s in dictWord:
            partitions.append(s)

        memo[s] = partitions 

        return memo[s]

    # def dfs(self, s, wordDict, memo):
    #     if s in memo:
    #         return memo[s]

    #     if len(s) == 0:
    #         return []

    #     partitions = []

    #     for i in range(1, len(s)):
    #         prefix = s[:i]
    #         if prefix not in wordDict:
    #             continue

    #         sub_partitions = self.dfs(s[i:], wordDict, memo)
    #         for partition in sub_partitions:
    #             partitions.append(prefix + " " + partition)

    #     if s in wordDict:
    #         partitions.append(s)

    #     memo[s] = partitions
    #     return partitions


if __name__ == "__main__":
    print(Solution().wordBreak("lintcode", [
          "de", "ding", "co", "code", "lint"]))
    print(Solution().wordBreak("a", [""]))
