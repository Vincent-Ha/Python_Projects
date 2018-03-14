import connectfour

# This dictionary refers to the drop and pop functions within the connectfour
# module. This dictionary is used in the _player_turn function.
connectfour_action = {'DROP' : connectfour.drop,
                      'POP' : connectfour.pop }

# This dictionary is used to determine the players of the game. It converts the
# enum-like thing into a string that can be used in printing to the console.
connectfour_players = { connectfour.NONE : 'None',
                        connectfour.RED : 'Red',
                        connectfour.YELLOW : 'Yellow' }

def print_board(state : connectfour.GameState) -> None:
    '''
    This function prints the current state of the board using the GameState
    tuple. It prints dots for unused spots and R and Y for the red player and
    yellow player respectively.
    '''
    for row in range(connectfour.BOARD_COLUMNS):
        print(row + 1, end = '\t')
    print()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if (state.board[column][row] == connectfour.NONE):
                print('.', end = '\t' )
            elif (state.board[column][row] == connectfour.RED):
                print('R', end = '\t')
            else:
                print('Y', end = '\t' )
        print()

def take_input() -> (str, int):
    '''
    This function is in charge of taking in the correct input for connectfour
    commands. The function continues to ask the player to put in the correct
    commands until they do. The function returns the commands in the form of
    a tuple.
    '''
    choice  = ''
    column_choice = ''
    
    while choice == '':
        choice = input('Please enter your choice of action: ')
        if not choice.upper() == 'DROP' and not choice.upper() == 'POP':
            choice = ''
            print('ERROR!')

    while column_choice == '':
        try:
            column_choice = int(input('Please enter the column on which you wish' +
                                      ' for the action to take place: '))
            if column_choice > 7 or column_choice < 1:
                print('ERROR!')
                column_choice = ''
        except ValueError:
            print('ERROR!')
            column_choice = ''

    return (choice.upper(), column_choice)

def _player_turn(state : connectfour.GameState,
                 ai_game : bool,
                 username = '') -> (connectfour.GameState, str, int):
    '''
    This function is in charge of coordinating one player's turn. It prints the
    board then takes the player's input. It then changes the GameState
    accordingly.
    '''
    print_board(state)
    print()

    if not ai_game:
        print('It is ' + connectfour_players[state.turn] + "\'s turn.")
        print('--------------------')
    else:
        print('Your Turn, ' + username)
        print('--------------------')
    
    while True:
        try:
            player_choice = take_input()
            return (connectfour_action[player_choice[0]](state, player_choice[1] - 1),
                    player_choice[0], player_choice[1])
        except connectfour.InvalidMoveError:
            print('ERROR!')
