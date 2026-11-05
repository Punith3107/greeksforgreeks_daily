class Solution:
    def getMinimumDays(self, s, p):
        a=[0]*len(s)
        for i,x in enumerate(p): a[x]=i+1
        return max([min(a[i],a[i+1]) for i in range(len(s)-1) if s[i]==s[i+1]]+[0])
