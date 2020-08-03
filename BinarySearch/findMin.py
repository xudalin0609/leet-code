# LintCode 159
"""

159. 寻找旋转排序数组中的最小值
中文English
假设一个排好序的数组在其某一未知点发生了旋转（比如0 1 2 4 5 6 7 可能变成4 5 6 7 0 1 2）。你需要找到其中最小的元素。

样例
样例 1:

输入：[4, 5, 6, 7, 0, 1, 2]
输出：0
解释：
数组中的最小值为0
样例 2:

输入：[2,1]
输出：1
解释：
数组中的最小值为1
注意事项
你可以假设数组中不存在重复元素。
"""

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None

        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right - 1:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid
            elif nums[mid] < nums[0]:
                right = mid
        return nums[right]


if __name__ == "__main__":
    print(Solution().findMin([4,5,6,0,1,2,3]))
    print(Solution().findMin([2, 1]))
    print(Solution().findMin([1, 2, 3]))
    print(Solution().findMin([6, 1, 2, 3,4,5]))
    print(Solution().findMin([4,5,6,7,0,1,2]))

