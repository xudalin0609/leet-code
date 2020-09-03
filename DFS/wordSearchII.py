# LintCode 132
"""
132. 单词搜索 II
中文English
给出一个由小写字母组成的矩阵和一个字典。找出所有同时在字典和矩阵中出现的单词。
一个单词可以从矩阵中的任意位置开始，可以向左/右/上/下四个相邻方向移动。一个字母在一个单词中只能被使用一次。且字典中不存在重复单词

样例
样例 1:

输入：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
输出：["again","can","dad","dog"]
解释：
  d o a f
  a g a i
  d c a n
矩阵中查找，返回 ["again","can","dad","dog"]。
样例 2:

输入：["a"]，["b"]
输出：[]
解释：
 a
矩阵中查找，返回 []。
挑战
使用单词查找树来实现你的算法
"""

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if not board:
            return []

        words_set = set(words)
        prefix_string = set([])

        for word in words:
            for i in range(len(word)):
                prefix_string.add(word[:i+1])
        
        print(prefix_string)

        results = set([])

        for x in range(len(board)):
            for y in range(len(board[x])):
                self.search(board,
                            x,
                            y,
                            board[x][y],
                            prefix_string,
                            words_set,
                            results,
                            set([(x, y)]))

        return list(results)

    def search(self, board, x, y, subtring, prefix_string, words_set, results, visited):
        if subtring not in prefix_string:
            return

        if subtring in words_set:
            results.add(subtring)

        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y


            if not self.is_inside(x_, y_, board):
                continue

            if (x_, y_) in visited:
                continue

            visited.add((x_, y_))
            self.search(board, x_, y_, subtring +
                        board[x_][y_], prefix_string, words_set, results, visited)
            visited.remove((x_, y_))

        return results

    def is_inside(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


if __name__ == "__main__":
    # print(Solution().wordSearchII(["doaf", "agai", "dcan"], [
    #       "dog", "dad", "dgdg", "can", "again"]))

    print(Solution().wordSearchII(
                       ["b", "a", "b", "b", "a"],
                       ["babbab", "b", "a", "ba"]
                       ))
