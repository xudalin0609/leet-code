"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Accepted

"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row_num in range(len(matrix)):
            if len(matrix[row_num]) < 1:
                return False
            if matrix[row_num][0] <= target:
                res = self.binarySearch(matrix[row_num], target, 0, len(matrix[row_num]))
                print(row_num, res)
                if res:
                    return res
        return False

    def binarySearch(self, arr, k, left, right):
        if right - left <= 1:
            if arr[left] == k:
                return True
            else:
                return False
        mid = (left + right) >> 1
        if arr[mid] > k:
            target = self.binarySearch(arr, k, left, mid)
        elif arr[mid] < k:
            target = self.binarySearch(arr, k, mid, right)
        else:
            return True
        return target


if __name__ == "__main__":
    arr = [
        []
    ]
    print(Solution().searchMatrix(arr, 1))
