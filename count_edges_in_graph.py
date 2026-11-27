class Solution:
    def countEdges(self, adj):
        return sum(len(x) for x in adj)//2
