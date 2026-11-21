class Solution:
    def smallestSubWithSum(self, arr, x):
        left=0
        total=0
        ans=len(arr)+1
        for right in range(len(arr)):
            total+=arr[right]
            while total>x:
                ans=min(ans,right-left+1)
                total-=arr[left]
                left+=1
        return ans if ans<=len(arr) else 0
