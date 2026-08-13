class Solution:
    def isValid(self, s: str) -> bool:
        o=['(','[','{']
        d={'(':')','[':']','{':'}'}
        l=[]
        for i in s:
            if i in o:
                l.append(i)
            else:
                if len(l)==0:
                    return False
                x=l[-1]
                if i==d[x]:
                    l.pop()
                else:
                    return False
        if len(l)==0:
            return True
        else:
            return False
        