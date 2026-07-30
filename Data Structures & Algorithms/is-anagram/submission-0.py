class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for j in t:
            if j not in d.keys() or d[j]==0 :
                return False
            else:
                d[j]-=1
        return True
        