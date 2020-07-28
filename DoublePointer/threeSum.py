# Lint Code 57
"""
57. 三数之和
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

样例
例1:

输入:[2,7,11,15]
输出:[]
例2:

输入:[-1,0,1,2,-1,-4]
输出:[[-1, 0, 1],[-1, -1, 2]]
注意事项
在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers is None:
            return None
        
        res = []
        numbers.sort()
        index = 0
        while index < len(numbers):
            left, right = index + 1, len(numbers) - 1
            while left < right:
                if numbers[index] + numbers[left] + numbers[right] > 0:
                    right -= 1
                elif numbers[index] + numbers[left] + numbers[right] < 0:
                    left += 1
                else:
                    res.append([numbers[index], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left - 1] == numbers[left]:
                        left += 1

                    while left < right and numbers[right + 1] == numbers[right]:
                        right -= 1
            index += 1
            while index < len(numbers) and numbers[index] == numbers[index - 1]:
                index += 1

        return res

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
    print(Solution().threeSum([-1,0,1,2,-1,-4, -1,0,1,2,-1,-4]))