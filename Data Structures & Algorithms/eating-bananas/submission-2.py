class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        k=r
        while l<r:
            m=(l+r)//2
            c=0
            for i in piles:
                #c+=math.ceil(i/m) or
                c+=(i+m-1)//m
            if c<=h:
                #k=min(k,m) or eventually when l==r l is the least k
                r=m# as c=h is also valid so here m is also valid no need r=m+1
            else:
                l=m+1
        return l




        