"""
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

 

示例 1：

输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：

输入：[60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整数。
 

提示：

1 <= time.length <= 60000
1 <= time[i] <= 500
通过次数10,850提交次数25,211
"""

class Solution:
    def numPairsDivisibleBy60_2(self, time):
        time_sorted = sorted(time, reverse=True)
        count = 0
        flag = 0

        if len(time_sorted) == 0:
            return count

        for t in range(len(time_sorted)):
            if time_sorted[t] < 60:
                break
            flag += 1
    
        for i in range(flag):
            while time_sorted[i] > 60:
                time_sorted[i] -= 60
            if time_sorted[i] == 0:
                count += 1
            else:
                for j in range(flag, len(time_sorted)):
                    if time_sorted[i] == time_sorted[j]:
                        count += 1

        return count

    def numPairsDivisibleBy60_1(self, time):
        # time_sorted = sorted(time)
        count = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                print(i, j)
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

    def numPairsDivisibleBy60_4(self, time):
        from collections import defaultdict
        hashmap = defaultdict(int)
        res = 0
        for t in time:
            if t % 60 in hashmap: res += hashmap[t % 60]
            if t % 60 == 0:
                hashmap[0] += 1
                continue
            hashmap[60 - t % 60] += 1
        return res


    def numPairsDivisibleBy60(self, time):
        dic={}
        count = 0
        for i,t in enumerate(time):
            r = t%60
            dic.setdefault(60-r,0)
            dic[60-r]+=1
        for k, v in dic.items():
            if k == 30 or k == 60:
                n = dic[k] 
                count += n*(n-1) // 2
            # print(dic)
            elif dic.get(60-k):
                count += dic[k]*dic[60-k]
                dic[k],dic[60-k] = 0, 0

        return count


if __name__ == "__main__":
    print(Solution().numPairsDivisibleBy60([30,20,150,20,40]))
    print(Solution().numPairsDivisibleBy60([60,60,60]))
    print(Solution().numPairsDivisibleBy60([439,407,197,191,291,486,30,307,11]))
    print(Solution().numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]))
    print(Solution().numPairsDivisibleBy60([269,230,318,468,171,158,350,60,287,27,11,384,332,267,412,478,280,303,242,378,129,131,164,467,345,146,264,332,276,479,284,433,117,197,430,203,100,280,145,287,91,157,5,475,288,146,370,199,81,428,278,2,400,23,470,242,411,470,330,144,189,204,62,318,475,24,457,83,204,322,250,478,186,467,350,171,119,245,399,112,252,201,324,317,293,44,295,14,379,382,137,280,265,78,38,323,347,499,238,110,18,224,473,289,198,106,256,279,275,349,210,498,201,175,472,461,116,144,9,221,473]))