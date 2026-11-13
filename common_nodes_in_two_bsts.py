class Solution:
    def findCommon(self, r1, r2):
        s1, s2 = [], []
        ans = []

        while True:
            while r1:
                s1.append(r1)
                r1 = r1.left

            while r2:
                s2.append(r2)
                r2 = r2.left

            if not s1 or not s2:
                break

            if s1[-1].data == s2[-1].data:
                n1 = s1.pop()
                n2 = s2.pop()
                ans.append(n1.data)
                r1 = n1.right
                r2 = n2.right

            elif s1[-1].data < s2[-1].data:
                r1 = s1.pop().right

            else:
                r2 = s2.pop().right

        return ans
