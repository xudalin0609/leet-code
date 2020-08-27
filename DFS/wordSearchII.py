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
# class Solution:
#     """
#     @param board: A list of lists of character
#     @param words: A list of string
#     @return: A list of string
#     """
#     DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
#     def wordSearchII(self, board, words):
#         # write your code here
#         if not words:
#             return []

#         results = []
#         for word in words:
#             self.dfs(board, 0, 0, [], results, word)
#         return results

#     def dfs(self, board, x_axis, y_axis, substring, results, word):
#         if substring == list(word):
#             results.append("".join(substring))
#             return


#         for x, y in self.DIRECTIONS:
#             if y_axis + y < 0 or y_axis + y >= len(board) or x_axis + x < 0 or x_axis + x >= len(board[y_axis]):
#                 continue
#             substring.append(board[y_axis + y][x_axis + x])
#             self.dfs(board, x_axis + x, y_axis + y, substring, results, word)
#             substring.pop()

#         return results


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
                prefix_string.add(word[:i])

        results = set([])
        visited = set([])

        for x in range(len(board)):
            for y in range(len(board[x])):
                self.search(board,
                            x,
                            y,
                            board[x][y], 
                            prefix_string,
                            words_set, 
                            results, 
                            visited)

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
            self.search(board, x_, y_, subtring + board[x_][y_], prefix_string, words_set, results, visited)
            visited.remove((x_, y_))

        return results

    def is_inside(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# class Solution:
#     """
#     @param board: A list of lists of character
#     @param words: A list of string
#     @return: A list of string
#     """
#     def wordSearchII(self, board, words):
#         if board is None or len(board) == 0:
#             return []
        
#         # pre-process
#         # 预处理
#         word_set = set(words)
#         prefix_set = set()
#         for word in words:
#             for i in range(len(word)):
#                 prefix_set.add(word[:i + 1])
        
#         result = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 c = board[i][j]
#                 self.search(
#                     board,
#                     i,
#                     j,
#                     board[i][j],
#                     word_set,
#                     prefix_set,
#                     set([(i, j)]),
#                     result,
#                 )
                
#         return list(result)
        
#     def search(self, board, x, y, word, word_set, prefix_set, visited, result):
#         if word not in prefix_set:
#             return
        
#         if word in word_set:
#             result.add(word)
        
#         for delta_x, delta_y in DIRECTIONS:
#             x_ = x + delta_x
#             y_ = y + delta_y
            
#             if not self.inside(board, x_, y_):
#                 continue
#             if (x_, y_) in visited:
#                 continue
            
#             visited.add((x_, y_))
#             self.search(
#                 board,
#                 x_,
#                 y_,
#                 word + board[x_][y_],
#                 word_set,
#                 prefix_set,
#                 visited,
#                 result,
#             )
#             visited.remove((x_, y_))
            
#     def inside(self, board, x, y):
#         return 0 <= x < len(board) and 0 <= y < len(board[0])


if __name__ == "__main__":
    print(Solution().wordSearchII(["doaf", "agai", "dcan"], [
          "dog", "dad", "dgdg", "can", "again"]))
