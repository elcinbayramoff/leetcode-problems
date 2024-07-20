class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        def checker(current):
            
            if matrix[index_row][index_col] == 0:
                matrix[index_row][index_col] = current

                rowSum[index_row]  = 10**9 if rowSum[index_row]-current == 0 else rowSum[index_row]-current
                colSum[index_col]  = 10**9 if colSum[index_col]-current == 0 else colSum[index_col]-current
        matrix = [[0]*len(colSum) for _ in range(len(rowSum))]

        while True:
            min_row = min(rowSum)
            min_col = min(colSum)
            # print(min_row, min_col)
            if min_row == 10**9 or min_col == 10**9:
                return matrix
            
            index_row = rowSum.index(min_row)
            index_col = colSum.index(min_col)
            # print(min_row, min_col)
            if min_row <= min_col:
                current = min_row
                checker(current)
                    
            else:
                current = min_col
                checker(current)
            # print(rowSum,colSum)