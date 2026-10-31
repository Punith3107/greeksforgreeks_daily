class Solution:
    def maxPackages(self, arr, totalTime):
        k = min(totalTime, len(arr))
        s = sum(arr[:k])
        ans = s

        for i in range(k, len(arr)):
            s += arr[i] - arr[i-k]
            ans = max(ans, s)

        return ans
