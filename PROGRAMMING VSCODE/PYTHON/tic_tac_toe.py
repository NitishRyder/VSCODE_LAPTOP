def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board, player):
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print("It's " + current_player + "'s turn.")
        position = int(input("Choose a position between 1 and 9: ")) - 1

        if board[position] != " ":
            print("That position is already taken. Try again.")
            continue

        board[position] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(current_player + " wins!")
            break

        if " " not in board:
            print("It's a tie!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

tic_tac_toe()
