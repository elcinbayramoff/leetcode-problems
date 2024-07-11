class Solution:
    def reverseParentheses(self, s: str) -> str:
        sol, res =[], []
        
        for i in s:
            
            if i == ")":
                last = sol.pop()
                
                while last != "(":
                    res.append(last)
                    last = sol.pop()
                    
                for j in res:
                    sol.append(j)
                res = []
                
            else:
                sol.append(i)
                
        return "".join(sol)
    
    
'''
Explaination:
We will have sol for creating answer, and res for reversing partions. Till the first ")"
we append all the chars to the sol, and if we find ")", we will reverse elements till the
last "(" and the last "(" will be removed also. It will continue till all the pairs reversed
 
'''
