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