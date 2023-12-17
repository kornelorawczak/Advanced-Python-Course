#in the given examples, 0 means an empty spot
test_board1 = [   #This sudoku puzzle has 1 solution
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

test_board2 = [   #This example has 4 solutions
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 0, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def next_empty(board): #this function takes the board as an argument and returns first found empty spot (returns None tuple if there isn't any)
    for y in range(9):
        for x in range(9):
            if board[y][x]==0: return (y,x)
    return (None, None)

def print_board(board):
    print("-------------------------")
    for y in range(9):
        for x in board[y]: print(x,end="  ")
        print("")
    print("-------------------------")

def is_valid(board, x, row, col): #this function checks if proposed number in an empty spot can be placed there
    return True if x not in board[row] and x not in [b[col] for b in board] \
                   and x not in [board[horizontal][vertical] for horizontal in range((row//3)*3,(row//3)*3+3) for vertical in range((col//3)*3,(col//3)*3+3)] else False


def sudoku_solver(board):
    row, col = next_empty(board)
    if row == None:
        yield board
        return
    for i in range(1, 10):
        if is_valid(board, i, row, col):
            board[row][col] = i
            yield from sudoku_solver(board)
            board[row][col]=0
            # For given number (i) function recursively calls itself with the number placed in empty spot
            # If sudoku cant be solved with placed number, function recursively backtracks and tries different possibility
    return False  # if there isn't any number (i) that can be placed in empty spot, this puzzle is unsolvable and returns False in result

def main():
    for solution in sudoku_solver(test_board2):
        print_board(solution)

if __name__ == "__main__":
    main()



