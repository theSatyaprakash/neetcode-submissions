class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(),key=lambda x :x[1],reverse=True)
        n=0
        while k:
            l.append(d[n][0])
            n+=1
            k-=1
        return l
        