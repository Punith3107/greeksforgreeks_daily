class Solution:
    def findPattern(self, s):
        i = 0
        n = len(s)
        while i < n:
            if s[i] != 'x':
                return False
            x = 0
            y = 0
            while i < n and s[i] == 'x':
                x += 1
                i += 1
            while i < n and s[i] == 'y':
                y += 1
                i += 1
            if x != y:
                return False
        return True
