"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

"""


class Solution:
    def diffWaysToCompute(self, input):
        input_list = []
        last = -1
        for i in range(len(input)):
            if input[i] in ["-", "*", "+"]:
                input_list.append(input[last+1:i])
                input_list.append(input[i])
                last = i
        input_list.append(input[last+1:])
        return self.subCompute(input_list)

    def subCompute(self, input):
        if len(input) <= 1:
            return input
        res =[]
        for loc, val in enumerate(input):
            if val in ["-", "*", "+"]:
                left = self.subCompute(input[:loc])
                right = self.subCompute(input[loc+1:])
                for l in left:
                    for r in right:
                        res.append(self.__compute(l, r, val))
        return res

    def __compute(self, num1, num2, symbol):
        num1 = int(num1)
        num2 = int(num2)
        if symbol == "+":
            return num1+num2
        elif symbol == "-":
            return num1-num2
        elif symbol == "*":
            return num1*num2


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("2*3-4*5"))
    # print(Solution().diffWaysToCompute("11"))
