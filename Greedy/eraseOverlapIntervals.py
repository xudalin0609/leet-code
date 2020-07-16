# 435
"""
给定多个区间，计算让这些区间互不重叠所需要移除区间的最少个数。起止相连不算重叠。
"""
"""
输入是一个数组，数组由多个长度固定为 2 的数组组成，表示区间的开始和结尾。输出一个
整数，表示需要移除的区间数量。
Input: [[1,2], [2,4], [1,3]]
Output: 1
"""

"""
在选择要保留区间时，区间的结尾十分重要：选择的区间结尾越小，余留给其它区间的空间
就越大，就越能保留更多的区间。因此，我们采取的贪心策略为，优先保留结尾小且不相交的区
间。
具体实现方法为，先把区间按照结尾的大小进行增序排序，每次选择结尾最小且和前一个选
择的区间不重叠的区间。我们这里使用 C++ 的 Lambda，结合 std::sort() 函数进行自定义排
序。
在样例中，排序后的数组为 [[1,2], [1,3], [2,4]]。按照我们的贪心策略，首先初始化为区间
[1,2]；由于 [1,3] 与 [1,2] 相交，我们跳过该区间；由于 [2,4] 与 [1,2] 不相交，我们将其保留。因
此最终保留的区间为 [[1,2], [2,4]]。
"""
"""
int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) {
        return 0;
    }
    int n = intervals.size();
    sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int> b) {
        return a[1] < b[1];
    });
    int total = 0, prev = intervals[0][1];
    for (int i = 1; i < n; ++i) {
        if (intervals[i][0] < prev) {
            ++total;
        } else {
            prev = intervals[i][1];
        }
    }
    return total;
}
"""

class Solution:
    
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if i[0] >= last_end:
                last_end = i[1]
            else:
                res += 1
        return res

if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,2]]))


