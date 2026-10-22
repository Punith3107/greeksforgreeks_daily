class Solution(object):
    def minimumSum(self, s):
        n = len(s)
        arr = list(s)
        for i in range(n // 2):
            j = n - 1 - i
            a, b = arr[i], arr[j]
            if a != '?' and b != '?':
                if a != b:
                    return -1
            elif a == '?':
                arr[i] = b
            else:
                arr[j] = a

        total = 0
        prev = None
        for c in arr[:(n + 1) // 2]:
            if c != '?':
                if prev is not None:
                    total += abs(ord(c) - ord(prev))
                prev = c
        return 2 * total
