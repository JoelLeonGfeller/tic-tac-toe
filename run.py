board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


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


my_board = ['#','X','O','O','X','X','O','X','O','O']

display_board(my_board)



def player_input():
    marker = ''

    while marker.lower() != 'x' and marker.lower() != 'o':
        marker = input('Please enter O or X: ')

    if marker.lower() == 'x':
        return('X','O')
    else:
        return('O','X')

player1, player2 = player_input()

print("Player1: "+player1+" Player2: "+player2)

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

    while position not in range(1,10) or not space_checker(board,position):
        position = input('Place your marker enter 1-9: ')

    return position 

def relpayy():
     player = input('Do you wanna play again? press "y" for yes')

     return play == 'y'

while True:
     
     board = [' ']*10

     player1, player2 - player_input()

     while true:
          #display board
          display_board(board)

         #check the position
         position - player_choice(board)

          #place that marker
          marker_placer(board,position,player1)

          #chek who wins
          if win_check:
             print("player 1 has won!")
             break
          elif not 
     
     
     