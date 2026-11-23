class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        
        class Solution:
            def findCharacter(self, s, pos):
                lengths=[len(s)]
                i=1
                while lengths[-1]<pos:
                    lengths.append(2*lengths[-1]+i)
                    i+=1
                for i in range(len(lengths)-1,0,-1):
                    prev=lengths[i-1]
                    if pos>prev+i:
                        pos=2*prev+i-pos+1
                    elif pos>prev:
                        return '$'
                return s[pos-1]
