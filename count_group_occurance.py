class Solution:
    def getCount(self, s, k):
        count = {}

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                count[s[i]] = count.get(s[i], 0) + 1

        ans = 0

        for ch in count:
            if count[ch] == k:
                ans += 1

        return ans
