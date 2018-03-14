'''
Vincent Ha
ID: 14788488
'''

import othello

def _start_game() -> 'Othello':
    '''
    This function starts the interaction with the user by asking for the size of
    the gameboard they wish to play Othello on, the player with the
    first turn and how the game is won. This information is used to create
    an Othello object with those specifications.
    '''
    print('FULL')

    info_list = []

    while (len(info_list) == 0):
        try:
            row = int(input())
            if (row % 2 == 1 or row < 4 or row > 16):
                print('ERROR')
                continue
            info_list.append(row)
            
            column = int(input())
            if (column % 2 == 1 or column < 4 or column > 16):
                print('ERROR')
                info_list = []
                continue
            info_list.append(column)
            
            first_turn_player = input().upper()
            if not (first_turn_player == 'B' or first_turn_player == 'W'):
                print('ERROR')
                info_list = []
                continue
            info_list.append(first_turn_player)
            
            win_condition = input()
            if not (win_condition == '>' or win_condition == '<'):
                print('ERROR')
                info_list = []
                continue
            
            info_list.append(win_condition)
            
        except ValueError:
            print('ERROR')
            info_list = []
            continue

    return othello.Othello(info_list[0], info_list[1], info_list[2],
                           info_list[3])

def _setup_game(gamestate : 'Othello') -> 'Othello':
    '''
    This function sets up of initial gameboard with specifications given by the
    user.
    '''
    board_setup = []
    for row in range(len(gamestate.gameboard)):
        while (True):
            row_setup = input()
            row_setup_list = row_setup.split(' ')
            
            for items in row_setup_list:
                if not(items == 'B' or items == 'W' or items == '.'):
                    row_setup_list = []
                    print('ERROR')
                    break

            if (row_setup_list == [] or len(row_setup_list) >
                len(gamestate.gameboard[0])):
                continue
                
            board_setup.append(row_setup_list)
            break

    gamestate.setup_game(board_setup)
    return gamestate

def _print_winner(gamestate : 'Othello') -> None:
    '''
    This function prints the winner on the board based on the win condition
    given by the user.
    '''
    print('WINNER: ' + gamestate.calculate_winner())
    
def _player_turn(gamestate : 'Othello', turn_player : str) -> str:
        '''
        This function handles one individual turn. It checks for valid input
        and for valid moves in the game.
        '''
        coordinates = input()
        
        try:
            row = int(coordinates.split(' ')[0]) - 1
            column = int(coordinates.split(' ')[1]) - 1

            if (row < 0 or row >= len(gamestate.gameboard)):
                return 'INVALID'
             
            if (column < 0 or column >= len(gamestate.gameboard)):
                return 'INVALID'
            
        except IndexError:
            return 'INVALID'

        except ValueError:
            return 'INVALID'
        
        valid = gamestate.player_turn(row, column, turn_player)
        
        if (valid): 
            return 'VALID'
        else:
            return 'INVALID'

def _gameplay (gamestate : 'Othello') -> None:
    '''
    This function runs the entire game of Othello by the user. It checks for
    any moves avaliable on the board as well as whether or not the user entered
    a valid move. It also checks for when the game is over, where the function
    would print out the winner of the game.
    '''
    turn_player = gamestate.first_player
    player_dict = {
        'B' : 'W',
        'W' : 'B'
    }
    no_moves = False
    move = ''
    show_board = True
    
    while not (gamestate.game_over()):
        if (not gamestate.any_valid_moves(turn_player)[0] and
            not gamestate.any_valid_moves(player_dict[turn_player])[0]
            or (gamestate.game_over())):

            # If given a winning board, get out of the loop and print winning
            # screen.
            break
        
        if (gamestate.any_valid_moves(turn_player)[0]): #prevents double printing
            gamestate.print_board()
        
        if not (gamestate.any_valid_moves(turn_player)[0]):
            if not (gamestate.any_valid_moves(player_dict[turn_player])[0]):
                break
            else:
                turn_player = player_dict[turn_player]
                continue

        print('TURN: ' + turn_player)
        while (True):
            move = _player_turn(gamestate, turn_player)
            print(move)
        
            if (move == 'VALID'):
                break
        
        no_moves = False
        turn_player = player_dict[turn_player]

    gamestate.print_board()
    _print_winner(gamestate)

def game():
    '''
    This function handles everything the program does, from setting up the
    gameboard to playing the game of Othello.
    '''
    gamestate = _start_game()
    gamestate = _setup_game(gamestate)
    _gameplay(gamestate)

'''
Main Function
'''
if __name__ == '__main__':
    game()

