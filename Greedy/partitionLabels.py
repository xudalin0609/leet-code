# 763

"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

 

示例 1：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

"""
"""
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans

"""
class Solution:
    def partitionLabels(self, S):
        import collections
        c = collections.Counter(S)
        temp = {}
        for i, s in enumerate(S):
            temp[s] = i
        sub_temp = {}
        res = [0]
        for i, s in enumerate(S):
            sub_temp[s] = i
            if temp.get(s) == i:
                sub_temp.pop(s)
                if len(sub_temp) == 0:
                    res.append(i+1-sum(res))
        res.pop(0)
        return res

if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

