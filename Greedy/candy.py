# leetcode 135

"""
一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一
个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；所
有孩子至少要有一个糖果。求解最少需要多少个糖果。

Input: [1,0,2]
Output: 5
"""

"""
做完了题目 455，你会不会认为存在比较关系的贪心策略一定需要排序或是选择？虽然这一
道题也是运用贪心策略，但我们只需要简单的两次遍历即可：把所有孩子的糖果数初始化为 1；
先从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的
糖果数加 1；再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数
不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加 1。通过这两次遍历，
分配的糖果就可以满足题目要求了。这里的贪心策略即为，在每次遍历中，只考虑并更新相邻一
侧的大小关系。
在样例中，我们初始化糖果分配为 [1,1,1]，第一次遍历更新后的结果为 [1,1,2]，第二次遍历
更新后的结果为 [2,1,2]
"""
"""
int candy(vector<int>& ratings) {
    int size = ratings.size();
    if (size < 2) {
        return size;
    }
    vector<int> num(size, 1);
    for (int i = 1; i < size; ++i) {
        if (ratings[i] > ratings[i-1]) {
            num[i] = num[i-1] + 1;
        }
    }
    for (int i = size - 1; i > 0; --i) {
        if (ratings[i] < ratings[i-1]) {
            num[i-1] = max(num[i-1], num[i] + 1);
        }
    }
    return accumulate(num.begin(), num.end(), 0); // std::accumulate 可以很方便
    地求和
    }
"""
class Solution:

    def candy(self, ratings):
        least_candies = [1]*len(ratings)
        length = len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and least_candies[i] <= least_candies[i-1]:
                least_candies[i] = least_candies[i-1]+1
        
        for i in range(2, len(ratings)+1):
            if ratings[length-i] > ratings[length-i+1] and least_candies[length-i] <= least_candies[length-i+1]:
                least_candies[length-i] = least_candies[length-i+1]+1
        print(least_candies)

        return sum(least_candies)


if __name__ == "__main__":
    print(Solution().candy([1,2,87,87,87,2,1]))