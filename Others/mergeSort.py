class MergeSort:
    def mergeSort(self, nums):
        self.nums = nums
        left = 0
        right = len(nums)
        self.__mergeSort(left, right)
        return self.nums

    def __mergeSort(self, left, right):
        if right - left <= 1:
            return
        mid = (left + right) >> 1
        self.__mergeSort(left, mid)
        self.__mergeSort(mid, right)
        self.__merge(left, right, mid)

    def __merge(self, left, right, mid):
        i, j = left, mid
        temp = []
        while i < mid and j < right:
            if self.nums[i] < self.nums[j]:
                temp.append(self.nums[i])
                i += 1
            elif self.nums[i] > self.nums[j]:
                temp.append(self.nums[j])
                j += 1
            else:
                temp.append(self.nums[i])
                temp.append(self.nums[j])
                i += 1
                j += 1
        while i < mid:
            temp.append(self.nums[i])
            i += 1
        while j < right:
            temp.append(self.nums[j])
            j += 1
        self.nums[left:right] = temp
        print(temp, left, right)
        print(self.nums)


if __name__ == "__main__":
    print(MergeSort().mergeSort([1, 5, 3, 5, 8, 2, 4, 8, 4, 1, 74, 5]))
