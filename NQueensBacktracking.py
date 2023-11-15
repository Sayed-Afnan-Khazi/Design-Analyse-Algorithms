'''N-Queens Algorithm using backtracking'''

n = 10 # Board size
# Initializing the board (n x n)
board = []
for yy in range(n):
    board.append([None]*n)

# True at a position will indicate a queen in that position

def printBoard():
    for prow in board:
        print(prow)


def is_queen_safe(row, col):
    global n
    n-=1

    # Checking if a queen is present on that row or column
    for i in range(n):
        if board[row][i] or board[i][col]:
            n+=1
            return False
        

    
    # Checking if a queen is present on that LR diagonal
    diagonal_start_row = row
    diagonal_start_column = col
    # Checking from the position till the start of the LR diagonal
    while diagonal_start_row >= 0 and diagonal_start_column >= 0:
        if board[diagonal_start_row][diagonal_start_column]:
            n+=1
            return False
        diagonal_start_row -= 1
        diagonal_start_column -= 1

    
    diagonal_start_row = row
    diagonal_start_column = col
    # Checking from the position to the end of the LR diagonal
    while diagonal_start_row <= n and diagonal_start_column <= n:
        if board[diagonal_start_row][diagonal_start_column]:
            n+=1
            return False
        diagonal_start_row += 1
        diagonal_start_column += 1




    # Checking if a queen is present on that RL diagonal
    diagonal_start_row = row
    diagonal_start_column = col
    # Checking from the position till the start of the RL diagonal
    while diagonal_start_row >= 0 and diagonal_start_column <= n:
        if board[diagonal_start_row][diagonal_start_column]:
            n+=1
            return False
        diagonal_start_row -= 1
        diagonal_start_column += 1


    diagonal_start_row = row
    diagonal_start_column = col
    # Checking from the position to the end of the RL diagonal
    while diagonal_start_row <= n and diagonal_start_column >= 0:
        if board[diagonal_start_row][diagonal_start_column]:
            n+=1
            return False
        diagonal_start_row += 1
        diagonal_start_column -= 1

    n+=1
    return True



def n_queens_backtracking(row):
    global n
    if row == n:
        print("Complete")
        printBoard()
        return True
    # printBoard()
    # print ("Doing row", row)
    for try_column in range(n):
        if is_queen_safe(row, try_column):
            # print(row, try_column, "is safe")
            board[row][try_column] = True
            next = n_queens_backtracking(row+1)
            if not next:
                # print ("BACKTRACKING")
                board[row][try_column] = None
            else:
                # printBoard()
                return True
        # else:
        #     print(row, try_column, "is not safe")
    else:
        return False



n_queens_backtracking(0)