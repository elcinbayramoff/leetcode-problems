class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if x > y: high, highval, low, lowval = 'ab',x, 'ba',y
        else: high, highval, low, lowval = 'ba',y, 'ab',x
        
        stack = []
        score = 0
        for i in s:
            if i == high[1] and len(stack) != 0 and stack[-1] == high[0]:
                stack.pop(-1)
                score += highval
            else:
                stack.append(i)
            
        s = ''.join(stack)
        stack = []
        for i in s:
            if i == low[1] and len(stack) != 0 and stack[-1] == low[0]:
                stack.pop(-1)
                score += lowval
            else:
                stack.append(i)
        return score