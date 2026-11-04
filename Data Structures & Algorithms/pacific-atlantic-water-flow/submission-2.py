

class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        row,col=len(h),len(h[0])
        p=set()
        a=set()
        res=[]
        def dfs(r,c,v,ht):
            if (r,c) in v or r>=row or c>=col or r<0 or c<0 or h[r][c]<ht:
                return
            if h[r][c]>=ht:
                v.add((r,c))
            dfs(r+1,c,v,h[r][c])
            dfs(r-1,c,v,h[r][c])
            dfs(r,c+1,v,h[r][c])
            dfs(r,c-1,v,h[r][c])
        for r in range(row):
            dfs(r,0,p,h[r][0])
            dfs(row-1-r,col-1,a,h[row-1-r][col-1])
        for c in range(col):
            dfs(0,c,p,h[0][c])
            dfs(row-1,c,a,h[row-1][c])
        for (r,c) in p:
            if (r,c) in a:
                res.append([r,c])
        return res