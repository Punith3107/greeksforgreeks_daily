class Solution:
    def pairsViolatingBST(self, root):
        vals = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            vals.append(cur.data)
            cur = cur.right

        n = len(vals)
        rank = {v: i + 1 for i, v in enumerate(sorted(vals))}
        bit = [0] * (n + 1)
        res = 0
        for idx in range(n - 1, -1, -1):
            r = rank[vals[idx]] - 1
            while r > 0:
                res += bit[r]
                r -= r & -r
            r = rank[vals[idx]]
            while r <= n:
                bit[r] += 1
                r += r & -r
        return res
