#Tic-tac-toe Game

def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
        
def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_draw(board):
    
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    players = ["X", "O"]
    current_player = 0

    print("Welcome to the Tic-Tac-Toe Game!")
    
    while True:
        print_board(board)
    
        move = input(f"Player {players[current_player]}'s turn. Enter your move (row, column): ")
        row, col = map(int, move.split(","))
        
       
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row-1][col-1] != " ":
            print("Invalid move. Try again.")
            continue
        
        board[row-1][col-1] = players[current_player]
        
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins! Congratulations!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player
        
tic_tac_toe()





























