class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        r=[0]*len(t)
        s=[]#nested list of temp and index
        for idx,temp in enumerate(t):
            while s and temp>s[-1][0]:
                stemp,sidx=s.pop()
                r[sidx]=(idx-sidx)
            s.append([temp,idx])
        return r


        
        