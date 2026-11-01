class Solution:
    def maximumSubarray(self, arr):
        a = b = ans = float('-inf')
        for x in arr:
            c = max(x, a+x)
            d = max(x*x, a+x*x, b+x)
            a, b = c, d
            ans = max(ans, a, b)
        return ans
