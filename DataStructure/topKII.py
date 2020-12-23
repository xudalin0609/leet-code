"""
545. 前K大数 II
中文English
实现一个数据结构，提供下面两个接口
1.add(number) 添加一个元素
2.topk() 返回前K大的数

样例
样例1

输入: 
s = new Solution(3);
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()
		
输出: 
[10, 3]
[1000, 10, 3]
[1000, 10, 4]
[1000, 100, 10]

解释:
s = new Solution(3);
>> 生成了一个新的数据结构, 并且 k = 3.
s.add(3)
s.add(10)
s.topk()
>> 返回 [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> 返回 [1000, 10, 3]
s.add(4)
s.topk()
>> 返回 [1000, 10, 4]
s.add(100)
s.topk()
>> 返回 [1000, 100, 10]
样例2

输入: 
s = new Solution(1);
s.add(3)
s.add(10)
s.topk()
s.topk()

输出: 
[10]
[10]

解释:
s = new Solution(1);
>> 生成了一个新的数据结构, 并且 k = 1.
s.add(3)
s.add(10)
s.topk()
>> 返回 [10]
s.topk()
>> 返回 [10]
"""
import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.heap = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.heap, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return heapq.nlargest(self.k, self.heap)
