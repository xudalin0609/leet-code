class Solution:

    def NumbersWithEqualDigitSum(self, nums):
        digts_dic = {i: [] for i in range(1, 91)}
        for i in range(len(nums)):
            digts_dic[self.ChangeNumToDigit(nums[i])].append(nums[i])

        temp = []
        for l in filter(lambda x: len(x) > 1, digts_dic.values()):
            temp.append(sum(sorted(l)[-2:]))

        if len(temp) >= 1:
            return max(temp)
        else:
            return -1

    def ChangeNumToDigit(self, num):
        res = 0
        for c in str(num):
            res += int(c)
        return res


if __name__ == "__main__":
    print(Solution().NumbersWithEqualDigitSum([42, 33, 60]))
