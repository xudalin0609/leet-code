# Lint code 148
"""

148. 颜色分类
中文English
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

样例
样例 1

输入 : [1, 0, 1, 2]
输出 : [0, 1, 1, 2]
解释 : 原地排序。
挑战
一个相当直接的解决方案是使用计数排序扫描2遍的算法。

首先，迭代数组计算 0,1,2 出现的次数，然后依次用 0,1,2 出现的次数去覆盖数组。

你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历一遍数组的算法？

"""


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                index += 1
                left += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1

        return nums

if __name__ == "__main__":
    print(Solution().sortColors([0,2,1,2,0,0,0,0,1,2,0]))
