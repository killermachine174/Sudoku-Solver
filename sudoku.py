letters = 'ABCDEFGHI'
digits = '123456789'

'''
A1 A2 A3| A4 A5 A6| A7 A8 A9
B1 B2 B3| B4 B5 B6| B7 B8 B9
C1 C2 C3| C4 C5 C6| C7 C8 C9    
---------+---------+---------   
D1 D2 D3| D4 D5 D6| D7 D8 D9    
E1 E2 E3| E4 E5 E6| E7 E8 E9   
F1 F2 F3| F4 F5 F6| F7 F8 F9    
---------+---------+---------  
G1 G2 G3| G4 G5 G6| G7 G8 G9    
H1 H2 H3| H4 H5 H6| H7 H8 H9    
I1 I2 I3| I4 I5 I6| I7 I8 I9  

Rules:

1) No duplicates in a square:
2) No duplicates in row:
3) No duplicates in column:

  
'''
# input for sudoku grid
line = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'


def change_to_grid(grid):
    """ This method changes the string grid to list """
    split_to_rows = [grid[i:i + 9] for i in range(0, len(grid), 9)]
    whole_grid = []

    for index in range(9):
        single_row = list(split_to_rows[index])
        whole_grid.append(single_row)
    return whole_grid


def is_complete(grid_name):
    if any('0' in sublist for sublist in grid_name):
        return False
    else:
        print_grid(grid_name)
        print("Board Complete")


def print_grid(grid_name):
    # for i in range(0,3):
    #     print(grid[0][i] + " ", sep='', end='', flush=True)
    # print("| ", sep='', end='', flush=True)
    # for i in range(3, 6):
    #     print(grid[0][i] + " ", sep='', end='', flush=True)
    # print("| ", sep='', end='', flush=True)
    # for i in range(6,9):
    #     print(grid[0][i] + " ", sep='', end='', flush=True)
    # print("| ", sep='', end='', flush=True)
    count = 0
    print("\n------+-------+--------")
    for k in range(9):
        for i in range(0, 9, 3):
            for j in range(i, i + 3):
                print(grid_name[k][j] + " ", sep='', end='', flush=True)
            print("| ", sep='', end='', flush=True)

        count = count + 1
        if count % 3 == 0:
            print("\n------+-------+--------", sep='', end='', flush=True)

        print("")


# calling the method and storing it.
my_grid = change_to_grid(line);

print_grid(my_grid)

is_complete(my_grid)
