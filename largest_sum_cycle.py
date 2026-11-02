class Solution:
    def largestSumCycle(self, edge):
        n=len(edge)
        seen=set()
        ans=-1
        for i in range(n):
            p={}
            u=i
            while u!=-1 and u not in seen and u not in p:
                p[u]=len(p)
                u=edge[u]
            if u in p:
                ans=max(ans,sum(list(p)[p[u]:]))
            seen.update(p)
        return ans
