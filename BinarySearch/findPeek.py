#LintCode 75
"""
75. 寻找峰值
中文English
你给出一个整数数组(size为n)，其具有以下特点：

相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。

样例
样例 1:
	输入:  [1, 2, 1, 3, 4, 5, 7, 6]
	输出:  1 or 6
	
	解释:
	返回峰顶元素的下标


样例 2:
	输入: [1,2,3,4,1]
	输出:  3

挑战
Time complexity O(logN)

注意事项
数组保证至少存在一个峰
如果数组存在多个峰，返回其中任意一个就行
数组至少包含 3 个数
"""
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        
        start, end = 1, len(A) - 2
        
        while start < end - 1:
            mid = (start + end) >> 1
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        
        if A[start] >= A[end]:
            return start
        else:
            return end

if __name__ == "__main__":
    print(Solution().findPeak([1,2,1,3,4,5,7,6]))
    print(Solution().findPeak([1,2,3,4,1]))