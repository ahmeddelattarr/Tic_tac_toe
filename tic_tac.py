from IPython.display import clear_output
import random

def display_board(board):
    print('\n'*100)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
   
def player_input():
    mark=''
    while not (mark=='x'or mark =='o'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker == 'x':
             return ('x', 'o')
        else:
            return ('o', 'x')
def place_maker(board, mark ,position):
    board[position]=mark
def win_check (board,mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
def who_gonna_play_first():
    if random.randint(0,1)==0:
        return 'player one goes first'
    else :
        return 'player two goes first'
def space_checker(board,position):
    return board[position] == ' '
def board_full (board):
    for i in range (1,10):
        if space_checker(board,i):
            return False
    return True
def player_choice(board):
    pos=0
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_checker(board,pos):
        pos = int(input('Choose your next position: (1-9) '))
    return pos
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = who_gonna_play_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player one goes first':  # Corrected the player name here
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 has won the game!')  # Corrected player name
                game_on = False
            else:
                if board_full(theBoard):  # Corrected function name here
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player two goes first'  # Corrected player name

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won!')  # Corrected player name
                game_on = False
            else:
                if board_full(theBoard):  # Corrected function name here
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player one goes first'  # Corrected player name

    if not replay():
        break