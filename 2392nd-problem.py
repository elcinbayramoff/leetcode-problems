class RowCol:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.left = None
def build_matrix(k,rowConditions, colConditions):
    dict = {}
k=3
dict = {}
for i in range(1,k+1):
    dict[i] = RowCol(i)
    
print(dict)

row1 = dict[1]
row1.prev = dict[2]
row3 = dict[3]
row3.prev = dict[2]

col2 = dict[2]
col2.left = dict[1]

col3 = dict[3]
col3.left = dict[2]


