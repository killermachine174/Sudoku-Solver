from copy import deepcopy
#pratyush also contributed
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

_______________________________________________________________________________________________
Huge inspiration from Solving Every Sudoku Puzzle by Peter Norvig http://norvig.com/sudoku.html
_______________________________________________________________________________________________

'''

# This is main grid from which sudoku will be solved.
# If intended this all can be left 0 to generate sudoku


grid = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'  # feeding a empty board
# grid = '600874010009036000000190800794600000001089400000410069070050090053907600902061047'
# grid = '900000207700063000040000800087040009009102078302900000600700100200006000800001600'

# This is a global variable used as board for whole program
board = []


def change_to_grid():
    """ This method changes the string grid to list """
    global grid
    global board
    split_to_rows = [grid[i:i + 9] for i in range(0, len(grid), 9)]

    for index in range(9):
        single_row = list(split_to_rows[index])
        board.append(single_row)
    return board


def zero_to_dot():
    """ This method removes all the zeros from the grid"""
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '0':
                board[i][j] = '.'


def print_grid(board_name):
    """ This method prints all the grid in systematic order"""
    count = 0
    print("\n------+-------+--------")
    for k in range(9):
        for i in range(0, 9, 3):
            for j in range(i, i + 3):
                print(board_name[k][j] + " ", sep='', end='', flush=True)
            print("| ", sep='', end='', flush=True)

        count = count + 1
        if count % 3 == 0:
            print("\n------+-------+--------", sep='', end='', flush=True)

        print("")


def solve_by_possibilities():
    global board
    while True:  # running until there are changes made on the board
        changes = False
        for x in range(9):
            for y in range(9):
                all_possibilities = get_all_possibilities(x, y)
                if not all_possibilities:  # if all_possibilities == false
                    continue
                if len(all_possibilities) == 0:  # if possibility is zero that means there is error on board
                    break
                if len(all_possibilities) == 1:  # if possibility is one that means that possibility is the answer
                    board[x][y] = all_possibilities[0]
                    changes = True
        if not changes:
            return


def get_all_possibilities(x, y):
    if board[x][y] != '.':
        return False

    # creating SET of numbers that a position might have
    # using SET as data type is huge advantages as this is unordered and position might change
    all_possibilities = {str(num) for num in range(1, 10)}
    # removing all the possibilities from values that we get form the row
    # remember x is the x-axis of the board or row &
    #          y is the y-axis of the board or column
    # here row and column are fixed as x and y

    for row in board[x]:
        all_possibilities -= set(row)  # for row

    # for column
    for index in range(9):
        all_possibilities -= set(board[index][y])

    # for a square in board we need to know where the square are of x and y
    # integer division helps a lot in this problem as we get the starting index of x and y
    # for e.g x is 7th row, which means if we integer divide it by 3, we get 2 and multiply by 3 will
    # help to get the exact square position on board which is 6

    x_of_square = (x // 3) * 3
    y_of_square = (y // 3) * 3

    # dividing the board into small board after we get the starting index of square
    small_square = board[x_of_square: x_of_square + 3]
    for index, row in enumerate(small_square):
        small_square[index] = row[y_of_square: y_of_square + 3]

    # again, removing all the possibilities from square
    for rows in small_square:
        for nums in rows:
            all_possibilities -= set(nums)

    return list(all_possibilities)


def guessing_and_backtracking():
    global board
    solve_by_possibilities()  # solving by possibility first then only moving to recursion
    if is_complete():  # program stops here if the board is complete and stops the recursion
        return True

    x, y = 0, 0
    for rowIndex, row in enumerate(board):
        for columnIndex, column in enumerate(board):
            # searches for empty spot at board & gets the coordinate to make a guess
            if board[rowIndex][columnIndex] == '.':
                x, y = rowIndex, columnIndex
    # gets all the possibilities at the coordinate and makes a guess
    all_possibilities = get_all_possibilities(x, y)
    for values in all_possibilities:
        copy_of_board = deepcopy(board)  # making a copy of board if guess is wrong
        board[x][y] = values
        result = guessing_and_backtracking()  # recursively calling method again to check if the board is solved.
        if result:
            return True
        else:
            board = copy_of_board  # bringing back the copy of board as if there is wrong guess on the board

    return False


def is_complete():
    """ This method checks if the board is complete or not"""
    global board
    # this basically is getting all the elements from rows, which is inside of board
    if any('.' in rows for rows in board):
        return False
    else:
        return True


def main():
    change_to_grid()  # can also return a board
    zero_to_dot()
    solve_by_possibilities()
    guessing_and_backtracking()
    if is_complete():
        print_grid(board)
        print("Complete Board!")
    else:
        print("ERROR ON BOARD!!!")


if __name__ == '__main__':
    # start of the program
    main()
