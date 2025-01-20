import sys

def main():
    game_status = True
    player = 'X'
    moves = 0
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Welcome to Tic Tac Toe\nCoded by Andre Laurin\n\nPlayer 1 is X and goes first.\nSelect a number from 0 to 9, 0 quits the game.\n")
    display_board(board)

    while (game_status == True):
        print(f"\nPlayer {player}, your move.")
        user_input = input()
        if user_input.isdigit() == True:
            result = int(user_input)
        if user_input.isdigit() == False:
            print("You need to select a number between 0 and 9. Try to not break my game.")
        elif result < 0 and result > 8:
            print("Enter a number between 0 and 8, what's with {result}")
        else:
            if result == 0: # User selected to quite the game
                sys.exit()
            else:
                result -= 1
                board[result] = player
                if player == "X":
                    player = "O"
                else: player = "X"
                display_board(board)
                moves += 1
                if moves > 8:
                    game_status = False
                    print("\nIt's a draw.")
                    new_game(game_status)

                winner = check_win(board)
                if winner == "X" or winner == "O":
                    print(f"\nCongratulations {winner}, you won the game")
                    game_status = False
                    new_game(game_status)

def display_board(board):
    print(f"[ {board[0]} ] [ {board[1]} ] [ {board[2]} ]")
    print(f"[ {board[3]} ] [ {board[4]} ] [ {board[5]} ]")
    print(f"[ {board[6]} ] [ {board[7]} ] [ {board[8]} ]")

# I think this is the long hard way to do it. But I am still learning and it worked
def check_win(board):
    # Check all rows
    if board[0] == 'X' and board [1] == 'X' and board[2] == 'X': return 'X'
    if board[0] == 'O' and board [1] == 'O' and board[2] == 'O': return 'O'
    if board[3] == 'X' and board [4] == 'X' and board[5] == 'X': return 'X'
    if board[3] == 'O' and board [4] == 'O' and board[5] == 'O': return 'O'
    if board[6] == 'X' and board [7] == 'X' and board[8] == 'X': return 'X'
    if board[6] == 'O' and board [7] == 'O' and board[8] == 'O': return 'O'
    # Check all columns
    if board[0] == 'X' and board [3] == 'X' and board[6] == 'X': return 'X'
    if board[0] == 'O' and board [3] == 'O' and board[6] == 'O': return 'O'
    if board[1] == 'X' and board [4] == 'X' and board[7] == 'X': return 'X'
    if board[1] == 'O' and board [4] == 'O' and board[7] == 'O': return 'O'
    if board[2] == 'X' and board [5] == 'X' and board[8] == 'X': return 'X'
    if board[2] == 'O' and board [5] == 'O' and board[8] == 'O': return 'O'
    # Check diaganol
    if board[0] == 'X' and board [4] == 'X' and board[8] == 'X': return 'X'
    if board[0] == 'O' and board [4] == 'O' and board[8] == 'O': return 'O'
    if board[2] == 'X' and board [4] == 'X' and board[6] == 'X': return 'X'
    if board[2] == 'O' and board [4] == 'O' and board[6] == 'O': return 'O'
    return 'N'

def new_game(game_status):
    print("\nWould you like to play another game (Y/N)?")
    while (game_status == False):
        user_input = input()
        if user_input == "Y" or user_input == 'y':
            main()
        elif user_input == "N" or user_input == 'n':
            print("\nUntil the next time, later.")
            game_status = True
        else: 
            print("\nSo is that a Y or a N")

if __name__ == '__main__':
    main()