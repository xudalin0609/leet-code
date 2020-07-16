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


if __name__ == '__main__':
    test = [4, 33, 5, 59, 54, 4]
    # test = [10, 7, 8, 9, 1, 5]
    print(quickSort().quickSort(test, 0, len(test)))
