class Solution:
    def subsequenceSum(self, s):
        mod = 10**9 + 7
        total = sum(int(ch) for ch in s)
        return (total * pow(2, len(s) - 1, mod)) % mod
