class Solution:
    def firstElementKTime(self, arr, k):
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

            if count[num] == k:
                return num

        return -1
