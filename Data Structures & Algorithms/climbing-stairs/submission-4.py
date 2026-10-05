class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            t=one
            one=one+two
            two=t
        return one
        '''
        c=0
        l=[]
        def dfs(d,l,c):
            if (sum(l)==n):
                c+=1
                return 
            l.append(d)
            dfs(1,l,c)
            l.pop()
            dfs(2,l,c)
        dfs(0,l,c)
        return c'''