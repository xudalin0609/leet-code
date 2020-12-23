"""
544. 前K大数
中文English
在一个数组中找到前K大的数

样例
样例1

输入: [3, 10, 1000, -99, 4, 100] 并且 k = 3
输出: [1000, 100, 10]
样例2

输入: [8, 7, 6, 5, 4, 3, 2, 1] 并且 k = 5
输出: [8, 7, 6, 5, 4]
"""
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        nums.sort(reversed=True)
        list.sort
        return nums[:k]