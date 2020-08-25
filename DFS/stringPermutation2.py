# LintCode 10
"""

10. 字符串的不同排列
中文English
给出一个字符串，找到它的所有排列，注意同一个字符串不要打印两次。

样例
样例 1：

输入："abb"
输出：
["abb", "bab", "bba"]
样例 2：

输入："aabb"
输出：
["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]

        results = set([])
        string = list(str)
        string.sort()
        self.dfs(string, 0, [], results, set([]))
        return list(results)

    def dfs(self, str, index, chars, results, used):
        if len(chars) == len(str):
            results.add(''.join(chars))
            return

        for i in range(len(str)):
            if i in used:
                continue

            if i > 0 and str[i] == str[i - 1] and i - 1 not in used:
                # 如果前一位和这一位相同，且前一位未被选择，去重
                continue

            chars.append(str[i])
            used.add(i)
            self.dfs(str, index + 1, chars, results, used) # 找到所有chars的结果
            used.remove(i)
            chars.pop()

if __name__ == "__main__":
    # print(Solution().stringPermutation2("abb"))
    print(Solution().stringPermutation2("aabb"))
    # print(Solution2().stringPermutation2("aabb"))
    # print(Solution().stringPermutation2("abcgabcdabc"))
