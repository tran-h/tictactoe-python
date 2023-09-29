
def row_winner(board):
    for row in board:
        winning_row = True
        for space in row:
            if space == ' ' or space != row[0]:
                winning_row = False
                break
        if winning_row:
            return True
    return False

def column_winner(board):
    for i in range(len(board)):
        winning_col = True
        for j in range(len(board)):
            if board[j][i] == ' ' or board[j][i] != board[0][i]:
                winning_col = False
                break
        if winning_col:
            return True
    return False

def diagonal_winner(board):
    topleft = board[0][0]
    topright = board[0][-1]
    winning_diag1 = True
    winning_diag2 = True
    for i in range(len(board)):
        if board[i][i] == ' ' or board[i][i] != topleft:
            winning_diag1 = False
        if board[i][-i-1] == ' ' or board[i][-i-1] != topright:
            winning_diag2 = False
    return winning_diag1 or winning_diag2

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

def play_move(board, player):
    print(f"{player}'s turn to play:")
    row = input()
    col = input()
    board[int(row)-1][int(col)-1] = player
    print(format_board(board))

def make_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(' ')
        board.append(row)
    return board

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    maxMoves = board_size * board_size
    player1move = True
    for _ in range(maxMoves):
        if player1move:
            play_move(board, player1)
            player1move = False
        else:
            play_move(board, player2)
            player1move = True
        if winner(board) == True and player1move == True:
            print_winner(player2)
            return
        elif winner(board) == True and player1move == False:
            print_winner(player1)
            return
    print_draw()

play_game(3, 'X', 'O')