#Solution 1

'''
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i for i in range(1, n+1)]
        start = 0
        while len(res) > 1:
            start = (k % len(res) + start - 1) % len(res)
            if (start + 1) >= len(res):
                num = res[0]
            else:
                num = res[start+1]
            res.pop(start)
            start = res.index(num)

        return res[0]  
'''
#Solution 2 - Instead of creating list from 1 to n, I did it with index 0 to n-1 so calculations became much more easier

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i for i in range(n)]
        start = 0
        while len(res) > 1: 
            start = (start + k-1) % len(res)
            res.pop(start)
        
        return res[0] + 1  
