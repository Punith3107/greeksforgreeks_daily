class Solution:
    def cntSubsets(self, arr, l, r):
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 1)

        for x in arr:
            freq[x] += 1

        p2 = [1] * (n + 1)

        for i in range(1, n + 1):
            p2[i] = (p2[i - 1] * 2) % MOD

        ans = 0
        ways = 1
        remaining = n

        for k in range(r + 1):
            if k > 0:
                if freq[k - 1] == 0:
                    break

                ways = ways * (p2[freq[k - 1]] - 1) % MOD
                remaining -= freq[k - 1]

            if k >= l:
                count = ways * p2[remaining - freq[k]]
                ans = (ans + count) % MOD

        return ans
