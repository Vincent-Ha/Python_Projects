import connectfour
import connectfour_shared
import connectfour_protocol
import socket

class InvalidServerError(Exception):
    '''
    This error is to indicate that the server may not be the correct server
    that we are looking for.
    '''
    pass

def whitespace_present(string : str) -> bool:
    '''
    This function looks for whitespaces within the username and returns a bool
    based on what it finds.
    '''
    if '\t' in string or ' ' in string or '\n' in string or '\r' in string:
        return True
    else:
        return False

    
def get_server_info() -> connectfour_protocol.connectfour_connection:
    '''
    This function askes the user for a host and port and continues to ask
    until it connects to a valid server at a valid port.
    '''
    while True:
        host = input('Please specify the host (IP Address or Host URL): ')
        port = ''
        while (port == ''):
            try:
                port = int(input('Please specify the port: '))
                if port < 0 or port > 65535:
                    port = ''
                    print('Invalid Port Number!')
            except ValueError:
                port = ''
                print('Invalid Port Number!')

        connection = []
        
        try:
            connection = connectfour_protocol.connect(host, port)
        except socket.gaierror:
            print('ERROR! Please Re-enter host and port.')
        except ConnectionRefusedError:
            print('ERROR! Please Re-enter host and port.')

        if(len(connection) == 3):
            return connection

def get_username() -> str:
    '''
    This function askes for a username and continues to until it recieves a
    proper username and returns it.
    '''
    username = '\n'
    while (whitespace_present(username)):
        username = input('Please enter a username: ')
        if (whitespace_present(username)):
            print('Invalid Username!')
    return username

def begin_game() -> (connectfour_protocol.connectfour_connection, str):
    '''
    This function starts the game with the AI. It askes for all the things
    necessary to start the game and returns a tuple with the username and
    connection to the server if everything is valid. If the server responses
    unusually, the function raises an exception.
    '''
    print('Welcome to the Networked Connect Four Game!')
    print()
    
    connection = get_server_info()
    username = get_username()
    
    try:
        connectfour_protocol.start_game(connection, username)
    except connectfour_protocol.ConnectFourProtocolError:
        print('Unexpected Server Behavior. Shutting Down.')
        connectfour_protocol.disconnect(connection)
        raise InvalidServerError

    print()
    return (connection, username)

def _user_turn(state : connectfour.GameState,
               connection : connectfour_protocol.connectfour_connection,
               username : str
               ) -> connectfour.GameState:
    '''
    This function implements a user's turn. It records the action the user takes
    then passes it on to the server. It then records the server's moves and
    returns the updated game state.
    '''
    commands = connectfour_shared._player_turn(state, True, username)
    state = commands[0]

    ai_command = connectfour_protocol.place_command(connection, (commands[1], commands[2]))
                
    if(ai_command[0] == 'WINNER'):
        return state

    try:
        server_move_state = connectfour_shared.connectfour_action[ai_command[0]](state, ai_command[1] - 1)
    except connectfour_protocol.InvalidMoveError:
        print('Unexpected Server Move. Shutting Down.')
        connectfour_protocol.disconnect(connection)
        raise InvalidServerError

    return server_move_state

def gameplay():
    '''
    This function processes the entire game with the AI as well as the setting
    up of the game.
    '''
    try:
        connection_and_username = begin_game()
        connection = connection_and_username[0]
        username = connection_and_username[1]
    except InvalidServerError:
        return
    
    ai_gamestate = connectfour.new_game()
    while(connectfour.winner(ai_gamestate) == connectfour.NONE):
        try:
            ai_gamestate = _user_turn(ai_gamestate, connection, username)
            print()
        except connectfour_protocol.ConnectFourProtocolError:
            print('Invalid Input. Please Try Again.')
        except connectfour_protocol.InvalidServerMoveError:
            print('Invalid Input. Please Try Again.')
        except InvalidServerError:
            return

    connectfour_shared.print_board(ai_gamestate)
    print()
    
    if(connectfour.winner(ai_gamestate) == connectfour.RED):
        print('Congratulations! You have won the game!')
    else:
        print('Sorry. The AI has won the game.')

    connectfour_protocol.disconnect(connection)
    

if __name__ == '__main__':
    gameplay()
