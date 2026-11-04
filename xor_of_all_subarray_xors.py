class Solution:
    def subarrayXor(self, arr):
        from functools import reduce
        return reduce(lambda x,y:x^y, arr[::2], 0) if len(arr)%2 else 0
