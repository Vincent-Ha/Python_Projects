'''
Vincent Ha
ID: 14788488
'''

class Othello:
    '''
    This class provides the necessary tools to initiated and play a game of
    Othello. It checks for any valid moves and places them when called by the
    user from the functions found in the othello_ui.py file.
    '''

    '''
    Utility Functions
    -----------------
    These functions help run and setup the othello game that this class
    represents.
    '''
    def __init__(self : 'Othello', rows : int, columns : int, first_player
                 : str, win_condition : str) -> 'Othello':
        '''
        Constructor for the Othello class. It initiates the first turn player,
        the win condition, and the look of the board used to play the game of
        Othello.
        '''
        self.NONE = 0
        self.WHITE = 1
        self.BLACK = 2
        
        self.num_of_rows = rows
        self.num_of_columns = columns
        self.first_player = first_player
        self.win_condition = win_condition
        self.player_dict = {
            '.' : self.NONE,
            'W' : self.WHITE,
            'B' : self.BLACK}

        self.gameboard = []
        for index1 in range(self.num_of_rows):
            self.gameboard.append([])
            for index2 in range(self.num_of_columns):
                self.gameboard[index1].append(self.NONE)

    def setup_game(self : 'Othello', setup : [[str]]) -> None:
        '''
        This member function initiates the gameboard with whatever the user
        wants the board to look like. It uses a list of lists of strings that
        are either B, W or . (periods) to represent black counters, white
        counters and empty spaces respectively.
        '''
        for index1 in range(len(setup)):
            for index2 in range(len(setup[index1])):
                    self.gameboard[index1][index2] = self.player_dict[
                        setup[index1][index2]]

    def _counter_count(self : 'Othello', player : str) -> int:
        '''
        This member function counts the number of counters of a specified type
        and returns the amount counted.
        '''
        count = 0
        for row in self.gameboard:
            for counter in row:
                if (counter == self.player_dict[player]):
                    count += 1
        return count

    def _index_increment(self : 'Othello', row : int, column : int,
                         diagonal_type : str) -> (int, int):
        '''
        This member function helps increment/decrement the row and column
        indexes appropriately based on the type of diagonal it is. This
        function is used in checking and flipping diagonal counters.
        '''
        if (diagonal_type == 'LEFT DIAGONAL TOP'):
            return (row - 1, column - 1)
        elif (diagonal_type == 'LEFT DIAGONAL BOTTOM'):
            return (row + 1, column + 1)
        elif (diagonal_type == 'RIGHT DIAGONAL TOP'):
            return (row - 1, column + 1)
        else:
            return (row + 1, column - 1)
    '''
    Checking Functions
    ------------------
    These functions check for soecific valid moves on a specified space given by
    the user.
    '''
    def _check_rows(self : 'Othello', row : int, column : int,
                    turn_player : str) -> (bool, bool):
        '''
        This member function checks if there is a valid move on a specified
        row and column for a specific player in the row. It checks for the
        proximity of friendly and enemy counters and for the presence of
        friendly counters across a row of enemy counters/
        '''
        row_checks = [False, False]
        enemy_counter = False
        start = [column - 1, column + 1]
        end = [-1, len(self.gameboard[row])]
        step = [-1, 1]

        for index in range(len(start)):
            for counter in range(start[index], end[index], step[index]):
                if (not self.gameboard[row][counter] ==
                    self.player_dict[turn_player] and not
                    self.gameboard[row][counter] == self.NONE):
                    
                    enemy_counter = True
                    
                elif (self.gameboard[row][counter] ==
                      self.player_dict[turn_player] and enemy_counter):
                    
                    row_checks[index] = True
                    break
                else:
                    break
            
            enemy_counter = False

        return (row_checks[0], row_checks[1])

    def _check_columns(self : 'Othello', row : int, column : int, turn_player
                      : str) -> (bool, bool):
        '''
        This member function searches for a valid placement within the column
        for a particular player. Like the check_rows function, it searches for
        the presence of a friendly counter across a column of enemy counters.
        '''
        column_checks = [False, False]
        enemy_counter = False
        start = [row - 1, row + 1]
        end = [-1, len(self.gameboard)]
        step = [-1, 1]

        for index in range(len(start)):
            for counter in range(start[index], end[index], step[index]):

                if (not self.gameboard[counter][column] == self.player_dict[
                    turn_player] and not self.gameboard[counter][column] ==
                    self.NONE):
                    
                    enemy_counter = True
                    
                elif (self.gameboard[counter][column] == self.player_dict[
                    turn_player] and enemy_counter):
                    
                    column_checks[index] = True
                    break
                else:
                    break

            enemy_counter = False

        return (column_checks[0], column_checks[1])

    def _check_diagonal(self : 'Othello', row : int, column : int,
                        turn_player : str, type_of_diagonal :
                        str) -> (bool, bool):
        '''
        This member function checks for valid diagonal moves for a player at
        a particular spot. This function in essence works the same way as
        the _check_rows and _check_columns functions in that it looks for
        a friendly counter across a diagonal of enemy counters. However, the
        implementation of this function is quite different from the other two.
        '''
        row_index = row
        column_index = column
        enemy_counter = False
        type_of_diagonal_list = [type_of_diagonal + ' TOP',
                                 type_of_diagonal + ' BOTTOM']
        diagonal_checks = [False, False]

        for index in range(len(type_of_diagonal_list)):
            while (row_index >= 0 and row_index < len(self.gameboard) and
                   column_index >= 0 and column_index < len(self.gameboard[0])):

                coordinates = self._index_increment(row_index, column_index,
                                                    type_of_diagonal_list[index])
                row_index = coordinates[0]
                column_index = coordinates[1]

                if (row_index < 0 or row_index > len(self.gameboard) or
                   column_index < 0 or column_index > len(self.gameboard[0])):
                    break

                try:
                    if (not self.gameboard[row_index][column_index] ==
                        self.player_dict[turn_player] and not
                        self.gameboard[row_index][column_index] == self.NONE):
                        enemy_counter = True
                        
                    elif (self.gameboard[row_index][column_index] ==
                          self.player_dict[turn_player] and enemy_counter):
                        diagonal_checks[index] = True
                        break
                    else:
                        break
                    
                except IndexError:
                    break
                
            row_index = row
            column_index = column
            enemy_counter = False
            
        return (diagonal_checks[0], diagonal_checks[1])

    def _check_all_diagonals (self : 'Othello', row : int, column : int,
                              turn_player : str) -> (bool, bool, bool, bool):
        '''
        This member function checks all the different diagonals that are
        possible and returns the results of those tests.
        '''
        
        left_diagonal = self._check_diagonal(row, column, turn_player,
                                             'LEFT DIAGONAL')
        right_diagonal = self._check_diagonal(row, column, turn_player,
                                              'RIGHT DIAGONAL')

        return left_diagonal + right_diagonal

    def _check_moves(self : 'Othello', row : int, column : int,
                    turn_player : str) -> (bool, (bool, bool, bool, bool,
                                                  bool, bool, bool, bool)):
        '''
        This function checks all the possible moves on a particular spot and
        sees if they are valid or not. Whether or not there is a valid move
        and the specific checks of each move are returned.
        '''
        if not (self.gameboard[row][column] == self.NONE):
            return (False, [])

        valid_move = False
        
        row_tuple = self._check_rows(row, column, turn_player)
        column_tuple = self._check_columns(row, column, turn_player)
        diagonal_tuple = self._check_all_diagonals(row, column, turn_player)

        move_tuple = row_tuple + column_tuple + diagonal_tuple

        if (True in move_tuple):
            valid_move = True

        return (valid_move, move_tuple)

    '''
    Placement Functions
    -------------------
    These functions places counters at the appropriate spots according to the
    type of move, the position of the original counter and the player.
    '''

    def _place_row_counters(self : 'Othello', row : int, column : int,
                            turn_player : str, left_oriented : bool) -> None:
        '''
        This function places counters on a row in the gameboard based on whether
        or not the valid move is to the left or right of the counter being
        placed.
        '''
        if (left_oriented):
            start = column
            end = -1
            step = -1

        else:
            start = column
            end = len(self.gameboard[row])
            step = 1

        for counter in range(start, end, step):
            if (self.gameboard[row][counter] == self.player_dict[turn_player]
                and not counter == column):
                break
            else:
                self.gameboard[row][counter] = self.player_dict[turn_player]

    def _place_column_counters(self : 'Othello', row : int, column : int,
                               turn_player : str, top_oriented : bool) -> None:
        '''
        This member function places counters on a column. Like the previous
        function, the placement is based on whether or not the valid move is
        above or below the counter being placed.
        '''
        if (top_oriented):
            start = row
            end = -1
            step = -1

        else:
            start = row
            end = len(self.gameboard)
            step = 1
            
        for counter in range(start, end, step):
            
            if (self.gameboard[counter][column] == self.player_dict[turn_player]
                and not counter == row):
                break
            else:
                self.gameboard[counter][column] = self.player_dict[turn_player]
        
    def _place_diagonal_counters(self : 'Othello', row : int, column : int,
                               turn_player : str, diagonal_type : str) -> None:
        '''
        This member function places counters on a diagonal. This placement is
        based on the type of diagonal is a valid move.
        '''

        self.gameboard[row][column] = self.player_dict[turn_player]
        
        coordinates = self._index_increment(row, column, diagonal_type)
        row_index = coordinates[0]
        column_index = coordinates[1]
        
        while not (self.gameboard[row_index][column_index] == self.player_dict[turn_player]):
            
            self.gameboard[row_index][column_index] = self.player_dict[
                turn_player]

            coordinates = self._index_increment(row_index, column_index,
                                                diagonal_type)
            row_index = coordinates[0]
            column_index = coordinates[1]

    def _place_counters(self : 'Othello', row : int, column : int,
                       turn_player : str, move_tuple : (bool, bool, bool, bool,
                                                        bool, bool, bool,
                                                        bool)) -> None:
        '''
        This member function handles all the different types of counter
        placement in one place.
        '''
        if (move_tuple[0]):
            self._place_row_counters(row, column, turn_player, True)

        if (move_tuple[1]):
            self._place_row_counters(row, column, turn_player, False)

        if (move_tuple[2]):
            self._place_column_counters(row, column, turn_player, True)

        if (move_tuple[3]):
            self._place_column_counters(row, column, turn_player, False)

        if (move_tuple[4]):
            self._place_diagonal_counters(row, column, turn_player,
                                          'LEFT DIAGONAL TOP')

        if (move_tuple[5]):
            self._place_diagonal_counters(row, column, turn_player,
                                          'LEFT DIAGONAL BOTTOM')

        if (move_tuple[6]):
            self._place_diagonal_counters(row, column, turn_player,
                                          'RIGHT DIAGONAL TOP')

        if (move_tuple[7]):
            self._place_diagonal_counters(row, column, turn_player,
                                          'RIGHT DIAGONAL BOTTOM')
            
    '''
    Player Turn Functions
    ---------------------
    These functions handle everything that has to do with the user interaction
    with the game and the board of Othello.
    '''
    def game_over(self : 'Othello') -> bool:
        '''
        This function checks for any empty spots left on the gameboard. If
        there is a spot, the function will return False. The function will
        returns True otherwise.
        '''
        for row in self.gameboard:
            for column in row:
                if column == self.NONE:
                    return False
        return True

    def calculate_winner (self : 'Othello') -> str:
        '''
        This function calculates who is the winner by first counting all the
        counters on the gameboard. The winner is ultimately determined by the
        win condition set in the initiation of the instantiation of the class.
        '''
        black_counters = self._counter_count('B')
        white_counters = self._counter_count('W')

        if (black_counters == white_counters):
            return 'NONE'

        if (self.win_condition == '>'):
            if (black_counters > white_counters):
                return 'B'
            else:
                return 'W'
        else:
            if (black_counters < white_counters):
                return 'B'
            else:
                return 'W'

    def print_board(self : 'Othello') -> None:
        '''
        This member function prints the current game board as it stands using
        dots, B's and W's to represent empty spaces, 
        '''
        print_str = ''
        
        print('B: ' + str(self._counter_count('B')) + '  W: ' +
              str(self._counter_count(
            'W')))
        for row in self.gameboard:
            for counter in row:
                if (counter == self.WHITE):
                    print_str += 'W '
                elif (counter == self.BLACK):
                    print_str += 'B '
                else:
                    print_str += '. '
                    
            print(print_str[:-1])
            print_str = ''
            
    def any_valid_moves(self : 'Othello', turn_player : str) -> (bool, [tuple]):
        '''
        This function checks if there are any moves avaliable for a particular
        player anywhere on the board. It checks each spot using the check_moves
        function. This returns a boolean that states whether or not there is a
        valid move and the avaliable moves there are for the player.
        '''
        any_valid_moves = False
        avaliable_moves = []

        for row in range(len(self.gameboard)):
            for column in range(len(self.gameboard[row])):
                move = self._check_moves(row, column, turn_player)
                if (move[0] == True):
                    any_valid_moves = True
                    avaliable_moves.append((row, column, move))

        return (any_valid_moves, avaliable_moves)
    
    def player_turn(self : 'Othello', row : int, column : int, turn_player :
                    str) -> bool:
        '''
        This member function handles the checking for any avaliable moves, the
        validity of a specified move and the placement of counters onto the
        board based on the move.
        '''
        moves = self.any_valid_moves(turn_player)
        if (moves[0]):
            for items in moves[1]:
                if (items[0] == row and items[1] == column):
                    self._place_counters(row, column, turn_player, items[2][1])
                    return True
        return False
