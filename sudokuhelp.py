# this is a test page

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s], [])) - {s})
             for s in squares)

TRIPLETS = [[0,1,2],[3,4,5],[6,7,8]]

ROW_ITER = [[(row,col) for col in range(0,9)] for row in range(0,9)]
COL_ITER = [[(row,col) for row in range(0,9)] for col in range(0,9)]
TxT_ITER = [[(row,col) for row in rows for col in cols] for rows in TRIPLETS for cols in TRIPLETS]

grid_num = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

print(squares)