from itertools import groupby


class Solution:

    def MinMovesToObtainString(self, s):
        s = list(s)
        count = 0
        if len(s) <= 2:
            return 0
        i = 0
        while i < len(s)-1:
            temp = i
            while i < len(s)-1 and s[i] == s[i+1]:
                i += 1
            count += (i-temp+1)//3
            i += 1
        return count


if __name__ == "__main__":
    print(Solution().MinMovesToObtainString("abbbb"))
