def parse_board():
    with open('input') as f:
        board = []
        for line in f.read().splitlines():
            line_list = [int(i) for i in (line.replace(".","-1").split())]
            line2int = list(line_list)
            board.append(line2int)
        return board


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == -1:
                return i, j 

    return None, None


def valid(guess, board, row, col):
    # check row values
    row_values = board[row]
    if guess in row_values:
        return False
    
    # check column values
    col_values = [board[i][col] for i in range(9)]
    if guess in col_values:
        return False
    
    # check square
    row_s = (row//3)*3
    col_s = (col//3)*3

    for i in range(row_s, row_s + 3):
        for j in range(col_s, col_s + 3):
            if board[i][j] == guess:
                return False
            
    return True


def solve_sudoku(board):
    row, col = find_empty(board)

    if row is None:
        return True
    
    for guess in range(1, 10):
        if valid(guess, board, row, col):
            board[row][col] = guess
            if solve_sudoku(board):
                return True
        board[row][col] = -1

    return False


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)


if __name__ == "__main__":
    board = parse_board()
    solve_sudoku(board)
    print_board(board)
