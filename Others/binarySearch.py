class Solution:

    def binary_search(self, l, k):
        left = 0
        right = len(l)

        def __binary_search(l, k, left, right):
            mid = int((left + right) / 2)
            if l[mid] == k:
                return mid
            elif l[mid] > k:
                return __binary_search(l, k, left=left, right=mid)
            elif l[mid] < k:
                return __binary_search(l, k, left=mid, right=right)
            elif mid == left:
                return -1

        return __binary_search(l, k, left, right)


if __name__ == "__main__":
    print(Solution().binary_search([1], 5))
