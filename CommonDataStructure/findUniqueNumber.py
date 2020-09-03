# LintCode 685
"""
685. 数据流中第一个唯一的数字
中文English
给一个连续的数据流,写一个函数返回终止数字到达时的第一个唯一数字（包括终止数字）,如果找不到这个终止数字, 返回 -1.

样例
样例1

输入： 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
输出： 3
样例2

输入：
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
输出： -1
样例3

输入：
[1, 2, 2, 1, 3, 4]
3
输出： 3
"""
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        nums_dic = {}

        # Write your code here
        for num in nums:
            nums_dic[num] = nums_dic.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1

        for num, count in nums_dic.items():
            if count == 1:
                return num
            
        return -1

if __name__ == "__main__":
    print(Solution().firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 5))
    print(Solution().firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 7))
    print(Solution().firstUniqueNumber([1,2,2,1,3,4], 3))