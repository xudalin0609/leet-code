# LintCode 134
"""
134. LRU缓存策略
中文English
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

样例
Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
"""
import heapq
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.__dict = {}
        self.keys = set()
        self.__used_cache = []
        self.proprity = 0

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        self.proprity += 1
        if key in self.__dict:
            self.__dict[key][0] += 1
            self.__dict[key][1] = self.proprity
        else:
            return -1
        return self.__dict[key][2]

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        used_times_obj = [1, self.proprity, key]
        self.proprity += 1
        if self.capacity > 0:
            self.capacity -= 1
            heapq.heappush(self.__used_cache, used_times_obj)
        else:
            items = heapq.heappop(self.__used_cache)
            heapq.heappush(self.__used_cache, used_times_obj)
            del self.__dict[items[2]]

        self.__dict[key] = used_times_obj


if __name__ == "__main__":
    lc = LRUCache(3)
    lc.set(1, 1)
    lc.set(2, 2)
    lc.set(3, 3)
    lc.set(4, 4)
    print(lc.get(4))
    print(lc.get(3))
    print(lc.get(2))
    print(lc.get(1))
    lc.set(5, 5)
    print(lc.get(1))
    print(lc.get(2))
    print(lc.get(3))
    print(lc.get(4))
    print(lc.get(5))
    # 输出
    # [4,3,2,-1,-1,-1, 3, 4,5]
    # 期望答案
    # [4,3,2,-1,-1, 2, 3,-1,5]

"""
题解： 涉及删除和移动操作，使用链表，链表是有序的，一直维护，近期最多使用的放于尾部，那么每次缓存达到上限的时候，删除头部即可，其余为链表的基础操作模拟即可。


/**
* 本参考程序由九章算法用户提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，授课老师均来自硅谷和国内的一线大公司在职工程师。
* - 现有的求职课程包括：九章算法班 2020升级版，算法强化班，算法基础班，北美算法面试高频题班，Java 高级工程师 P6+ 小班课，面试软技能指导 - BQ / Resume / Project 2020版
* - Design类课程包括：系统设计 System Design，面向对象设计 OOD
* - 专题及项目类课程包括：动态规划专题班，Big Data - Spark 项目实战，Django 开发项目课
* - 更多详情请见官方网站：http://www.jiuzhang.com/?utm_source=code
*/
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):	#将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        
        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        prev = self.key_to_prev[key]
        current = prev.next
        
        self.kick(prev)
        return current.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        
        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
            self.pop_front()					#删除头部
"""