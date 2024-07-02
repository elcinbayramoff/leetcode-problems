#44ms
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        length = len(arr)
        if length <= 2:
            return False
        def finder(first,second,third):
            if third >= length:
                return False
            if arr[second] % 2 == 0:
                return finder(third,third+1,third+2)
            elif arr[second] % 2 == 0:
                return finder(second,third,third+1)
            elif arr[third] % 2 == 0:
                return finder(third+1,third+2,third+3)
            else:
                return True
        return finder(0,1,2)      

#49ms
'''
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False     
'''