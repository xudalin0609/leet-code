"""
486. 合并k个排序数组
中文English
将 k 个有序数组合并为一个大的有序数组。

样例
Example 1:

Input: 
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Example 2:

Input:
  [
    [1,2,3],
    [1,2]
  ]
Output: [1,1,2,2,3]
挑战
在 O(N log k) 的时间复杂度内完成：

N 是所有数组包含的整数总数量。
k 是数组的个数。
"""

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        merge_array = []
        k = len(arrays)
            
