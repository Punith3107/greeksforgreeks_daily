class Solution:
    def countBT(self, h: int) -> int:
        # code here
        if h <= 1:
            return 1
        a, b = 1, 1
        for i in range(2, h + 1):
            a, b = b, (b*b + 2*a*b) % 1000000007
        return b
