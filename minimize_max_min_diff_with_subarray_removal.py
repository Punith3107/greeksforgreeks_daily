
from collections import deque

class Solution:
    def minDiff(self, k, arr):
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        preMin, preMax = [0]*n, [0]*n
        sufMin, sufMax = [0]*n, [0]*n

        for i in range(n):
            preMin[i] = min(arr[i], preMin[i-1] if i else arr[i])
            preMax[i] = max(arr[i], preMax[i-1] if i else arr[i])

        for i in range(n-1, -1, -1):
            sufMin[i] = min(arr[i], sufMin[i+1] if i < n-1 else arr[i])
            sufMax[i] = max(arr[i], sufMax[i+1] if i < n-1 else arr[i])

        ans = float('inf')

        for i in range(n-k+1):
            if i == 0:
                mn, mx = sufMin[k], sufMax[k]
            elif i+k == n:
                mn, mx = preMin[i-1], preMax[i-1]
            else:
                mn = min(preMin[i-1], sufMin[i+k])
                mx = max(preMax[i-1], sufMax[i+k])

            ans = min(ans, mx-mn)

        return ans
