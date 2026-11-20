class Solution:
    def minFlips(self, s):
        a=0
        b=0
        for i in range(len(s)):
            if s[i]!=str(i%2):
                a+=1
            else:
                b+=1
        return min(a,b)
