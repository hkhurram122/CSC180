'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''
import random
import sys

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
 
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
   
   
def get_coord(square_num):
    coord = []
    if square_num > 0 and square_num < 10:
        coord.append((square_num - 1) // 3) # row
        coord.append((square_num - 3*coord[0])-1) # column
        return coord 
      

def put_in_board(board, mark, square_num):
    coord = get_coord(square_num)
    board[coord[0]][coord[1]] = mark


def is_free(board, square_num):
    coord = get_coord(square_num)
    free_squares = get_free_squares(board)
    if coord in free_squares:
        return True
    return False


# Problem 2

# a 
def get_free_squares(board):
    """Return a new list which contains a list of the coordinates
    of the FREE squares in the board"""

    coordinates = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'O' and board[i][j] != 'X':
                coordinates.append([i, j])

    return coordinates


# b
def make_random_move(board, mark):
    """Finds a random free square in board, and puts string mark 
    in the FREE square"""

    free_squares = get_free_squares(board)
    rand_index = int(len(free_squares) * random.random())

    rand_square = free_squares[rand_index]

    if mark == 'O':
        board[rand_square[0]][rand_square[1]] = mark



# problem 3

def is_row_all_marks(board, row_i, mark):
    """Return True iff the row with index row_i in board
    contains 3 marks equal to mark"""

    if (board[row_i].count(mark) == 3):
        return True
    else:
        return False


def is_col_all_marks(board, col_i, mark):
    """Returns True iff the col with index row_i in board
    contains 3 marks equal to mark"""   
    
    for j in range(len(board)):
        if board[j][col_i] != mark:
            return False
    return True
    

def is_diag_all_marks(board, mark):
    """Returns True iff one of the diags has all elements
    equal to mark"""
    diagonals = [[1,5,9],[3,5,7]]
    diag_ct = 0

    for diag in diagonals:
        for coords in diag:
            coord = get_coord(coords)
            if board[coord[0]][coord[1]] == mark:
                diag_ct += 1

        if (diag_ct == 3):
            return True 
        else:
            diag_ct = 0

    return False


def is_win(board, mark):
    """Returns True iff the mark mark won on the board board"""
  
    for a in range(3):
        if (is_diag_all_marks(board, mark) or is_col_all_marks(board, a, mark)
        or is_row_all_marks(board, a, mark)):
            print(f"The winner is: {mark}")
            return True
    if len(get_free_squares(board)) == 0: # list is empty
        print("Tie")
        return True
    return False # does not find a winning match 


# problem 4

def bot_win_move(board, mark):
    """Tries to put the computer's mark in every free square
    on the board, and checks whether is_win() returns True"""
    
    # instead of removing the mark, make a copy board to make checks 
    board_cpy = [] 
    for a in range(len(board)): # deep copy
        row = []           
        for b in range(len(board[0])):
            row.append(board[a][b])

        board_cpy.append(row)


    free_squares = get_free_squares(board)
    
    for i in range(len(free_squares)):
        board_cpy[free_squares[i][0]][free_squares[i][1]] = mark
        if is_win(board_cpy, mark): # the copy results in a bot win, change the real board 
            board[free_squares[i][0]][free_squares[i][1]] = mark
            return True 
        else:
            board[free_squares[i][0]][free_squares[i][1]] = " "
    return False
    
    
def user_play(board, mark):
    print(mark)
    input_str = 0
    while (not 0 < int(input_str) < 10) or (not is_free(board, input_str)):
        input_str = int(input("Enter your move: "))

    put_in_board(board, mark, input_str)
    print_board_and_legend(board)


def bot_play(board, mark):
    print(mark)


    if not bot_win_move(board, mark): # no such square for an immediate win
        make_random_move(board, mark)

    print_board_and_legend(board)

    
def game_start(game_end, board, mark):
    while not is_win(board, mark):
        if (mark == 'X'):
            user_play(board, mark)
            mark = 'O'
            continue 
        if (mark == 'O'): 
            bot_play(board, mark)
            if is_win(board, mark):
                break
            else:
                mark = 'X'
    sys.exit()


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    print_board_and_legend(board)           
    game_end = False
    mark = "X"
    game_start(game_end, board, mark)
