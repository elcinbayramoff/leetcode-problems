class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        dict = {
            'full': numBottles,
            'empty': 0
        }
        res = 0
        while dict['full'] > 0:
            res += dict['full']
            dict['empty'] += dict['full']
            dict['full'] = dict['empty'] // numExchange
            dict['empty'] %= numExchange
        return res