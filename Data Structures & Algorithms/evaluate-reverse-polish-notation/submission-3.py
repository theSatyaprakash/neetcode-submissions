class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=["+","-","*","/"]
        s=[]
        if not tokens:
            return 
        for i in tokens:
            if i in l:
                a=int(s.pop())
                b=int(s.pop())
                match i:
                    case "+":
                        s.append(b + a)
                    case "-":
                        s.append(b - a)
                    case "*":
                        s.append(b * a)
                    case "/":
                        s.append(int(b / a))
                
            else:
                s.append(i)
        return int(s[0])