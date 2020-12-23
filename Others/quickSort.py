class quickSort:

    def quickSort(self, nums, left, right):
        if right - left <= 1:
            return
        pi = self.partation(nums, left, right)
        self.quickSort(nums, left, pi)
        self.quickSort(nums, pi + 1, right)
        return nums

    def partation(self, nums, left, right):
        pivot = nums[right - 1]
        i, j = left, right - 2
        while i < j:
            while nums[i] <= pivot and i < j:
                i += 1
            if nums[i] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        if nums[i] > pivot:
            nums[right - 1], nums[i] = nums[i], nums[right - 1]
        return i
    

class QuickSortII:

    def quick_sort(self, nums):
        return self.__helper(nums, 0, len(nums) - 1)

    def __helper(self, nums, left, right):
        # print(nums)
        if left < right:
            pivot = self.partition(nums, left, right)
            self.__helper(nums, left, pivot - 1)
            self.__helper(nums, pivot + 1, right)
        return nums
    
    def partition(self, nums, left, right):
        """
        docstring
        """
        pivot = left
        while left < right:
            while left < right and nums[left] < nums[pivot]:
                left += 1
            while left < right and nums[right] >= nums[pivot]:
                right -= 1

            nums[right],nums[left] = nums[left], nums[right]
        nums[pivot],nums[left] = nums[left], nums[pivot]
        return left


if __name__ == '__main__':
    test = [4, 33, 5, 59, 54, 4]
    # test = [10, 7, 8, 9, 1, 5]
    print(QuickSortII().quick_sort(test))
