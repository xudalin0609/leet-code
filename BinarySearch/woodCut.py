# LintCode 183
"""
183. 木材加工
中文English
有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

样例
样例 1

输入:
L = [232, 124, 456]
k = 7
输出: 114
Explanation: 我们可以把它分成114cm的7段，而115cm不可以
样例 2

输入:
L = [1, 2, 3]
k = 7
输出: 0
说明:很显然我们不能按照题目要求完成。
挑战
O(n log Len), Len为 n 段原木中最大的长度

注意事项
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。
"""
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        
        if sum(L) < k:
            return 0

        L.sort()
        lo, hi = 1, L[-1]
        while lo < hi - 1:
            mid = (lo + hi) >> 1
            if self.woodIncludeSections(L, mid) < k:
                hi = mid
            else:
                lo = mid
        return lo

    
    def woodIncludeSections(self, L, section_length):
        return sum([_ // section_length for _ in L])
    
if __name__ == "__main__":
    print(Solution().woodCut([232, 124, 456], 7))