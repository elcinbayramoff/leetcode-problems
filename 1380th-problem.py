class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minimums = []
        res = []
        
        for i in matrix:
            minimums.append(min(i))
        for j in range(len(matrix[0])):
            if max([i[j] for i in matrix]) in minimums:
                res.append(max([i[j] for i in matrix]))
        return res