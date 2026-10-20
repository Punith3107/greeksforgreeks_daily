class Solution:
    def lexicographicallyLargest(self, arr):
        n = len(arr)
        res = []
        i = 0
        while i < n:
            j = i
            p = arr[i] & 1
            while j < n and (arr[j] & 1) == p:
                j += 1
            res.extend(sorted(arr[i:j], reverse=True))
            i = j
        return res
