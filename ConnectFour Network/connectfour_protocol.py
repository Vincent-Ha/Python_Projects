from collections import namedtuple
import socket
import connectfour

# This named tuple holds all the things required for communicating with the server.
connectfour_connection = namedtuple('connectfour_connection',
                                    ['socket', 'input', 'output'])

class ConnectFourProtocolError(Exception):
    '''
    This exception handles errors in which the server responds in an unexpected way.
    '''
    pass

class InvalidServerMoveError(Exception):
    '''
    This exception handles when the server gives an errorenous input as a connectfour command.
    This ideally should not be called at all since the server should offer correct moves.
    '''
    pass

def connect(host : str, port : int) -> connectfour_connection:
    '''
    This function is used to connect to the serve initially. It creates a socket and creates "pseudo-
    files" in order to write and read from the server.
    '''
    connectfour_socket = socket.socket()
    
    connectfour_socket.connect((host, port))

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return connectfour_connection (socket = connectfour_socket,
                                   input = connectfour_input,
                                   output = connectfour_output)

def disconnect(connection : connectfour_connection) -> None:
    '''
    This function closes all connections to the server.
    '''
    connection.socket.close()
    connection.input.close()
    connection.output.close()
    
def start_game(connection : connectfour_connection, username : str) -> None:
    '''
    This function starts the interaction with the proper server. It firsts says hello to the server
    with the given username then selects the AI_GAME function of the server. If there is unexpected
    server behavior, a ConnectFourProtocolError is called.
    '''
    _write_line(connection, 'I32CFSP_HELLO ' + username)      
    response = _read_line(connection)

    if (response == 'WELCOME ' + username):
        _write_line(connection, 'AI_GAME')
        response = _read_line(connection)
        if response == 'READY':
            return 
        else:
            raise ConnectFourProtocolError
    else:
        raise ConnectFourProtocolError

def place_command(connection : connectfour_connection,
                  command : (str, int)) -> (str, int):
    '''
    This function handles giving commands to the server directly. It properly forms the message the
    server expects and sends it. It then recieves the message that the server returns and processes
    it accordingly.
    '''
    responses = [] # Holds all the responses that the server returns.
    current_response = '' # Holds a specific individual response from the server.
    _write_line(connection, command[0] + ' ' + str(command[1]))
    while (not current_response == 'READY'):
        current_response = _read_line(connection)
        responses.append(current_response)
        
        if (current_response == 'INVALID'):
            raise InvalidServerMoveError
        
        if('WINNER' in current_response):
            if (len(responses) > 2 or len(responses) == 2):
                command = responses[1].split()
                return (command[0], int(command[1]))
            else:
                return ('WINNER',0)
    
    command = responses[1].split()
    return (command[0], int(command[1]))

def _write_line(connection : connectfour_connection, message : str) -> None:
    '''
    This function writes messages to the server.
    '''
    connection.output.write(message + '\r\n')
    connection.output.flush()

def _read_line(connection : connectfour_connection) -> str:
    '''
    This function reads the messages that the server gives to the user.
    '''
    return connection.input.readline()[:-1]
