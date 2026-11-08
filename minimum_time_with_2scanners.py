class Solution:
    def minTime(self, n, s1, s2):
        low, high = 0, n * min(s1, s2)

        while low < high:
            mid = (low + high) // 2

            if mid // s1 + mid // s2 >= n:
                high = mid
            else:
                low = mid + 1

        return low
