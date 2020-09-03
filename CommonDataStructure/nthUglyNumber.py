# LintCode 4
"""
4. 丑数 II
中文English
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

样例
样例 1：

输入：9
输出：10
样例 2：

输入：1
输出：1
挑战
要求时间复杂度为 O(nlogn) 或者 O(n)。

注意事项
我们可以认为 1 也是一个丑数。
"""
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set()
        for _ in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)

        return val


if __name__ == "__main__":
    print(Solution().nthUglyNumber(1))
