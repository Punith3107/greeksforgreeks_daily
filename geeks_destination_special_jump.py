class Solution:
    def minTime(self, a, b, d, l, r):
        mod=10**9+7
        c=a-b

        def reach(x):
            k=max(0,(x-a+c-1)//c)
            return x+2*b*k

        def pref(x):
            n=max(0,x-a)
            q,t=divmod(n,c)
            return c*q*(q+1)//2+t*(q+1)

        def total(L,R):
            if L>R:
                return 0
            n=R-L+1
            return (L+R)*n//2+2*b*(pref(R)-pref(L-1))

        normal=reach(d)
        lo,hi=1,d-1
        cut=0

        while lo<=hi:
            mid=(lo+hi)//2
            if reach(mid)+1<normal:
                cut=mid
                lo=mid+1
            else:
                hi=mid-1

        L=d-r
        R=d-l
        end=min(R,cut)
        cnt=max(0,end-L+1)

        ans=total(L,end)+cnt+(r-l+1-cnt)*normal
        return ans%mod
