# 88
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        print('f', id(nums1))
        tmp = nums1[:]
        print('f', id(tmp))
        tmp = nums1[:]
        nums1 = nums1[:m]
        print('s', id(nums1))
        for i in range(n):
            while j<m and nums2[i] > nums1[j]:
                j += 1
            if j >= m:
                nums1 += nums2[i:]
                print(nums1, id(nums1))
                return
            nums1.insert(j, nums2[i])

nums1 = [1,2,3,0,0,0]
print(nums1, id(nums1))
m = 3
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1,m,nums2,n))
print(nums1)

