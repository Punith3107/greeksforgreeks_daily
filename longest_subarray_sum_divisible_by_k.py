class Solution:
    def longestSubarrayDivK(self, arr, k):
        mp={0:-1}
        total=0
        ans=0
        for i in range(len(arr)):
            total+=arr[i]
            r=total%k
            if r in mp:
                ans=max(ans,i-mp[r])
            else:
                mp[r]=i
        return ans

