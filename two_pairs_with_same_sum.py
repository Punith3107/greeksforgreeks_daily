class Solution:
    def findPairs(self, arr):
        n=len(arr)
        mp={}
        for i in range(n):
            for j in range(i+1,n):
                s=arr[i]+arr[j]
                mp.setdefault(s,[]).append((i,j))
        ans=None
        for pairs in mp.values():
            deg={}
            count=0
            pos=-1
            for k in range(len(pairs)-1,-1,-1):
                a,b=pairs[k]
                if count>deg.get(a,0)+deg.get(b,0):
                    pos=k
                deg[a]=deg.get(a,0)+1
                deg[b]=deg.get(b,0)+1
                count+=1
            if pos!=-1:
                a,b=pairs[pos]
                for c,d in pairs[pos+1:]:
                    if a!=c and a!=d and b!=c and b!=d:
                        cur=(a,b,c,d)
                        if ans is None or cur<ans:
                            ans=cur
                        break
        return list(ans) if ans else [-1,-1,-1,-1]
