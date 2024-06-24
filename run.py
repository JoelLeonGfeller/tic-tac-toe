def display_board(board):
    print("   |     |  ")
    print(board[1]+'  |  '+board[2]+'  | '+board[3])
    print('___|_____|___ ')
    print("   |     |  ")
    print(board[4]+'  |  '+board[5]+'  | '+board[6])
    print('___|_____|___')
    print("   |     |  ")
    print(board[7]+'  |  '+board[8]+'  | '+board[9])
    print("   |     |  ")


def player_input():
    marker = ''

    while marker.lower() != 'x' and marker.lower() != 'o':

        text = 'Please enter O or X: '

        marker = input(text)

    if marker.lower() == 'x':
        return('X','O')
    else:
        return('O','X')


def win_check(board,mark):
        return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def space_checker(board,position):
     if board[position] == ' ':
          return True
     return False

def marker_placer(board,position,mark):
     board[position]=mark

def player_choice(board):
    position = 0

    while True:
        try:
            position = int(input('Place your marker enter 1-9: '))
            if position in range(1,10) or space_checker(board,position):
                return position
            else:
                print("Invalid input. Please enter a valid position (1-9).")

        except ValueError:
            print("Invalid input. Please enter a number (1-9).")


def replay():
    play = input('Do you wanna play again? press "y" for Yes ')

    return play == 'y'


print("Welcome to the Tic tac toe game!")

while True:
     
    board = [' ']*10

    player1, player2 = player_input()

    turn = 'player1'

    while True:
        if turn=='player1':
            #display board
            display_board(board)

            #check the position
            position = player_choice(board)

            #place that marker
            marker_placer(board,position,player1)

            #check who wins
            if win_check(board,player1):
               display_board(board)
               print("Player 1 has won!")
               break
            elif space_checker(board,position):
               display_board(board)
               print('Match Tied')
               break
            else:
               turn = 'player2'
        else:
            #display board
            display_board(board)

            #check the position
            position = player_choice(board)

            #place that marker
            marker_placer(board,position,player2)

            #check who wins
            if win_check(board,player2):
               display_board(board)
               print("Player 2 has won!")
               break
            elif space_checker(board,position):
               display_board(board)
               print('Match Tied')
               break
            else:
               turn = 'player1'

    if not replay():
        break
     
     