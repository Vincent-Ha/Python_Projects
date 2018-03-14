import connectfour
import connectfour_shared

def _begin_game() -> connectfour.GameState:
    '''
    This program begins the console game of Connect Four. It starts with a
    greeting and a brief summary of directions in order to play the game.
    The function ends by returning a board of a new game.
    '''
    print('Welcome to Connect Four!', end = '\n\n')
    print('Please enter the action you want to take. The two actions avaliable' +
          ' are DROP and POP. DROP is to place a disc in a specified column and' +
          ' POP is to take out your own disc at a specified column.\n')
    
    board_game = connectfour.new_game()
    return board_game

def _full_game(state : connectfour.GameState) -> None:
    '''
    This function controls the flow of the game. It allows for each player to
    continue to play until there is a winner, in which the function prints the
    winning board before announcing the winner and end the function.
    '''
    while (connectfour.winner(state) == connectfour.NONE):
        state = connectfour_shared._player_turn(state, False)[0]
        print()
        
    connectfour_shared.print_board(state)
    print()
    print('Player ' + connectfour_shared.connectfour_players[state.turn]
          + ' has won the game!')

def program_UI() -> None:
    '''
    This function runs the entire program. The function grabs the GameState
    tuple from the _begin_game function and uses it to run the rest of the
    game.
    '''
    game_state = _begin_game()
    _full_game(game_state)


if __name__ == '__main__':
    program_UI()
