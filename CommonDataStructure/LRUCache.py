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

class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.root = LinkedNode()
        self.__cache = {}
        self.last_node = None
        self.first_node = None
   
    # @return an integer
    def get(self, key):
        pass

    def pop_first(self):
        del self.__cache[self.first_node.value]
        self.first_node = self.first_node.next

    def put_last(self, node):
        self.last_node.next = node
        self.last_node = node

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.capacity > 0:
            self.capacity -= 1
            self.__cache[key] = LinkedNode(key, value)
            return

        if key in self.__cache:
            self.put_last(self.__cache[key])
        else:
            self.pop_first()
            node = LinkedNode(key, value)
            self.put_last(node)
            self.__cache[key] = node

        

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