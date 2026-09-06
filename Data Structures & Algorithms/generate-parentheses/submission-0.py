class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        stack=[]
        def back(openn,close):
            if openn==close==n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                back(openn+1,close)
                stack.pop()
            if close<openn:
                stack.append(")")
                back(openn,close+1)
                stack.pop()
        back(0,0)
        return res
               

                