class Solution:
    def maximumWeight(self, n, edges, queries):
        p=list(range(n+1)); s=[1]*(n+1)
        def f(x):
            if p[x]!=x: p[x]=f(p[x])
            return p[x]
        e=sorted(edges,key=lambda x:x[2])
        ans=[0]*len(queries)
        j=total=0
        for q,i in sorted((q,i) for i,q in enumerate(queries)):
            while j<len(e) and e[j][2]<=q:
                u,v,_=e[j]
                a,b=f(u),f(v)
                if a!=b:
                    total+=s[a]*s[b]
                    p[a]=b
                    s[b]+=s[a]
                j+=1
            ans[i]=total
        return ans
