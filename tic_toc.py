import random


#### Global variables
the_new_board = [' '] * 10


def display_board(board):
    print('\n'*100)
    print( board[7]+3*" "+ "|" + board[8] +3*" " + "|" + board[9])
    print("-------------")
    print( board[4]+3*" "+ "|" + board[5] +3*" " + "|" + board[6])
    print("-------------")
    print( board[1]+3*" "+ "|" + board[2] +3*" " + "|" + board[3])
#############################################
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input (' Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#############################################
def place_marker(board, marker, position):
    board[position] = marker

###############################################

def win_check(board, mark):
    return (( board[7] == board [8] == board[9] == mark ) or
            (board[4] == board [5] == board[6] == mark) or
            (board[1] == board [2] == board[3] == mark) or
            (board[7] == board [4] == board[1] == mark) or
            (board[8] == board [5] == board[2] == mark) or
            (board[9] == board [6] == board[3] == mark) or
            (board[7] == board [5] == board[3] == mark) or
            (board[9] == board [5] == board[1] == mark))

#####################################################
def choose_first():
    ran = random.randint(0,1)
    if ran == 0:
        return 'Player 2'
    else:
        return 'Player 1'
#########################################################
def space_check(board, position):
    return board[position] == ' '
###########################################################
def full_board_check(board):

    return ' ' not in board[1:]
############################################################3
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        try:
            position = int(input(' Choose your next position: (1-9) '))
        except:
            print("I'm sorry, please try again.")

    return position
##############################################################
def replay():
    return input(' Do you want to continue the game? (Yes or No) ').lower().startswith('y')

#################################################################3
print('Welcome to Tic Tac Toe!')

while True:


    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will start the game.')

    play_game = input( 'Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(the_new_board)
            position = player_choice(the_new_board)
            place_marker(the_new_board,player1_marker,position)

            if win_check(the_new_board,player1_marker):
                display_board(the_new_board)
                print('Congratulations! You won the game!')
                game_on = False

            else:
                if full_board_check(the_new_board):
                    display_board(the_new_board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'
        else:


            display_board(the_new_board)
            position = player_choice(the_new_board)
            place_marker(the_new_board,player2_marker,position)

            if win_check(the_new_board,player2_marker):
                display_board(the_new_board)
                print('Player 2 win!')
                game_on = False

            else:
                if full_board_check(the_new_board):
                    display_board(the_new_board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
