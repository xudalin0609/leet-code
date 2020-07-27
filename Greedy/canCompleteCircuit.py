# LintCode 187
"""

187. 加油站
中文English
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第_i_个加油站前往第_i_+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。

样例
样例 1:

输入:gas[i]=[1,1,3,1],cost[i]=[2,2,1,1]
输出:2
样例 2:

输入:gas[i]=[1,1,3,1],cost[i]=[2,2,10,1]
输出:-1
挑战
O(n)时间和O(1)额外空间

注意事项
数据保证答案唯一。
"""

class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) - sum(cost) < 0:
            return -1

        tol_remain = gas[0] - cost[0]
        start_site = [0, tol_remain]
        for site_loction in range(len(gas)):
            tol_remain = tol_remain + gas[site_loction] - cost[site_loction]
            if tol_remain < start_site[1]:
                start_site = [site_loction, tol_remain]

        return start_site[0] + 1
            

if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1,1,3,1], [2,2,10,1]))
    print(Solution().canCompleteCircuit([1,1,3,1], [2,2,1,1])) # 2
    print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(Solution().canCompleteCircuit([2,0,1,2,3,4,0],[0,1,0,0,0,0,11] )) # 1
