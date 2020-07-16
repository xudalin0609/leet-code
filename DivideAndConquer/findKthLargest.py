"""

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""


class Solution:
    def findKthLargest(self, nums, k):
        self.k = k
        self.nums = nums
        return self.__findKthLargest(nums, 0, len(nums) - 1)

    def __findKthLargest(self, nums, left, right):
        pi = self.getKth(nums, left, right)
        if pi > self.k - 1:
            res = self.__findKthLargest(nums, left, pi - 1)
        elif pi < self.k - 1:
            res = self.__findKthLargest(nums, pi + 1, right)
        else:
            return nums[pi]
        return res

    def getKth(self, arr, low, high):
        j = low-1  # index of smaller element
        pivot = arr[high]  # pivot

        for i in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[i] >= pivot:
                # increment index of smaller element
                j += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[j+1], arr[high] = arr[high], arr[j+1]
        return j+1


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().findKthLargest([-1, 2, 0], 1))
