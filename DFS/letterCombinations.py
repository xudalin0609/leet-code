# LintCode 425
"""
425. 电话号码的字母组合
中文English
给一个不包含0和1的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。

下图的手机按键图，就表示了每个数字可以代表的字母。
1     | 2 ABC |3 DEF
4 GHI | 5 JKL |6 MNO
7 PQRS| 8 TUV |9 WXYZ
样例
样例 1:

输入: "23"
输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
解释: 
'2' 可以是 'a', 'b' 或 'c'
'3' 可以是 'd', 'e' 或 'f'
样例 2:

输入: "5"
输出: ["j", "k", "l"]
注意事项
以上的答案是按照词典编撰顺序进行输出的，不过，在做本题时，你也可以任意选择你喜欢的输出顺序。
"""
# BFS
# class Solution:
#     """
#     @param digits: A digital string
#     @return: all posible letter combinations
#     """
#     number_letter_dic = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"

#     }
#     def letterCombinations(self, digits):
#         # write your code here
#         if not digits:
#             return []

#         if len(digits) == 1:
#             return [_ for _ in self.number_letter_dic[digits]]

#         stack = [_ for _ in self.number_letter_dic[digits[0]]]
#         for num in digits[1:]:
#             tmp_stack = []
#             while stack:
#                 tmp_combination = stack.pop()
#                 for letter in self.number_letter_dic[num]:
#                     tmp_stack.append(tmp_combination + letter)
#             stack += tmp_stack

#         return stack

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, [], results)
        
        return results
    
    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append("".join(chars))
            return
        
        for letter in KEYBOARD[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, results)
            chars.pop()


if __name__ == "__main__":
    print(Solution().letterCombinations("234"))
    print(Solution().letterCombinations(""))