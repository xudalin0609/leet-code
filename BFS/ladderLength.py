# LintCode 120
"""
120. 单词接龙
中文English
给出两个单词（start和end）和一个字典，找出从start到end的最短转换序列，输出最短序列的长度。

变换规则如下：

每次只能改变一个字母。
变换过程中的中间单词必须在字典中出现。(起始单词和结束单词不需要出现在字典中)
样例
样例 1:

输入：start = "a"，end = "c"，dict =["a","b","c"]
输出：2
解释：
"a"->"c"
样例 2:

输入：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
输出：5
解释：
"hit"->"hot"->"dot"->"dog"->"cog"
注意事项
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
"""

import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)

        queue = collections.deque([start])
        distance = 0
        visited = set()
        start_word_len = len(start)
        if start_word_len < 1:
            return 0


        while queue:
            distance += 1
            
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                    
                self.find_next(word, queue, dict, visited)
        return 0

    
    def find_next(self, word, queue, dict, visited):
        word_len = len(word)

        for level in range(word_len):
            for letter in "qwertyuiopasdfghjklzxcvbnm":
                if word[level] == letter:
                    continue

                combined_word = word[:level] + letter + word[level+1:]
                if combined_word in dict and combined_word not in visited:
                    visited.add(combined_word)
                    queue.append(combined_word)

if __name__ == "__main__":
    print(Solution().ladderLength(start ="hit", end = "cog", dict =set(["hot","dot","dog","lot","log"])))
