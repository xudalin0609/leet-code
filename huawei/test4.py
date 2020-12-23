# 一道华为的面试题,输入一个target，找到所有能够组成这个target的连续子数组
# 面试的时候写出了暴力解法，想出了这个动态规划的方法，然而实现的时候有点乱，没写完（sad），这里补上
class Test:

    def test1(self, target):
        if not target or target <= 1:
            return []

        pre_subsets = {0: 0}
        last_sum = 0
        end = target // 2 + 1
        res = []
        for i in range(1, end + 1):
            diff = target - i
            pre_subset_val = last_sum - diff
            pre_subsets[last_sum + i] = i
            last_sum += i
            if pre_subset_val in pre_subsets:
                res.append(
                    [_ for _ in range(pre_subsets[pre_subset_val] + 1, i + 1)])

        return res

print(Test().test1(9))
