'''
Name : Vincent Ha
Student ID : 14788488
'''

import othello
import othello_point

class Counter:
    '''
    This class represents an individual counter on an Othello gameboard. It
    holds the center and space that this counter occupies. It also can
    tell whether or not a point is inside this counter space.
    '''
    def __init__(self : 'Counter', center : othello_point.Point,
                 radius : float, horizontal_distance : float,
                 vertical_distance : float) -> 'Counter':
        '''
        This constructor initializes the counter object with the center and
        radius of the circular counter. The horizontal distance and vertical
        distance is used for rectanglar grids to detect whether a point is
        inside this counter's spot.
        '''
        self.center = center
        self.radius = radius
        self.horizontal_distance = horizontal_distance
        self.vertical_distance = vertical_distance

    def get_center(self : 'Counter') -> 'othello_point.Point':
        '''
        This member function is an accessor to the center variable.
        '''
        return self.center

    def get_radius(self : 'Counter') -> float:
        '''
        This member fucntion is an accessor to the radius variable
        '''
        return self.radius

    def inside_circle(self : 'Counter', p : 'othello_point.Point') -> bool:
        '''
        This member function determines whether or not a point was inside a
        counter's occupied space. It returns this fact as a bool.
        '''
        if (self.center.distance_from_frac(p) < self.radius):
            return True

        c_points = self.center.to_frac()
        p_points = p.to_frac()

        if (p_points[0] > c_points[0] - self.horizontal_distance and
            p_points[0] < c_points[0] + self.horizontal_distance and
            p_points[1] > c_points[1] - self.vertical_distance and
            p_points[1] < c_points[1] + self.vertical_distance):
            return True
        
        else:
            return False        

class CounterPositions:
    '''
    The CounterPositions class holds information about the counters held within
    the Othello gameboard. It handles locating and recording where the counters
    of each player was placed in the gameboard.
    '''
    def __init__(self : 'CounterPositions', rows : int, columns : int,
                 first_turn_player : str, win_condition : str) \
                 -> 'CounterPositions':
        '''
        The constructor for the CounterPositions class. It holds an Othello
        object to handle the game logic of Othello. The counter locations
        held what and where the counters were placed on the board. Spot
        coordinates hold the positions of each grid within the Othello board.
        Initial setup holds the information for the initial gameboard state.
        '''
        self.gameboard = othello.Othello(rows, columns, first_turn_player,
                                    win_condition)
        self.counter_locations = []
        self.spot_coordinates = []
        self.initial_setup = []
        
        for row_index in range(rows):
            
            self.initial_setup.append([])
            self.spot_coordinates.append([])
            
            for column_index in range(columns):
                new_spot = othello_point.from_frac(
                             (row_index + row_index + 1) / (2 * rows),
                             (column_index + column_index + 1) / (2 * columns))

                if (1/rows) <= (1/columns):
                    end_point = othello_point.from_frac(
                        row_index / rows,
                        (column_index + column_index + 1) / (2 * columns))

                else:
                    end_point = othello_point.from_frac(
                        (row_index + row_index + 1) / (2 * rows),
                        column_index / columns)
                
                new_radius = new_spot.distance_from_frac(end_point)

                new_counter = Counter(new_spot, new_radius,
                                      1 / (2 * rows), 1 / (2 * columns))
                
                self.spot_coordinates[row_index].append(new_counter)
                self.initial_setup[row_index].append('.')

    def setup_placement(self : 'CounterPositions', x : int, y : int,
                        width : int, height : int, player : str) -> None:
        '''
        This member function handles placing and recording where a counter of
        a player is located during the setup phase. It places this information
        in both the counter_coordinates variable and the initial setup variable.
        '''
        temp_point = othello_point.from_pixel(x, y, width, height)
        
        for row_index in range(len(self.spot_coordinates)):
            for column_index in range(len(self.spot_coordinates[row_index])):
                
                if (self.spot_coordinates[row_index][column_index].\
                    inside_circle(temp_point)):

                    if(self.initial_setup[row_index][column_index] == '.'):
                        
                        self.initial_setup[row_index][column_index] = player
                        self.counter_locations.append(
                            (player,
                             self.spot_coordinates[row_index][column_index]))
                        return

    def setup_delete(self : 'CounterPositions', x : int, y : int, width : int,
                     height : int, player : str) -> None:
        '''
        This member function handles removing counters from the gameboard during
        the setup phase. The removal is recorded in both counter_coordinates and
        initial_setup.
        '''
        temp_point = othello_point.from_pixel(x, y, width, height)

        for row_index in range(len(self.spot_coordinates)):
            for column_index in range(len(self.spot_coordinates[row_index])):
                
                if (self.spot_coordinates[row_index][column_index].\
                    inside_circle(temp_point)):

                    if(self.initial_setup[row_index][column_index] == player):
                        
                        self.initial_setup[row_index][column_index] = '.'
                        
        for point in range(len(self.counter_locations)):
            if (self.counter_locations[point][1].inside_circle(temp_point)
                and self.counter_locations[point][0] == player):
                
                del self.counter_locations[point]
                return

    def finish_setup(self : 'CounterPositions') -> None:
        '''
        This member function finalizes the setup phase by placing the initial
        board into the Othello object.
        '''
        self.gameboard.setup_game(self.initial_setup)

    def flip_counters(self : 'CounterPositons', player : str) -> None:
        '''
        This function looks through the gameboard and flips the colors of
        counters that were flipped by the placing of a counter.
        '''
        temp_point = ()
        coordinates = (0,0)
  
        for row_index in range(len(self.gameboard.gameboard)):
            for column_index in range(len(self.gameboard.gameboard[row_index])):
                
                if not (self.gameboard.gameboard[row_index][column_index] == \
                        self.gameboard.NONE):
                   if (self.gameboard.gameboard[row_index][column_index] \
                            == self.gameboard.player_dict[player]):

                       point = self.spot_coordinates[row_index][column_index].\
                               get_center()

                       coordinates = point.to_frac()

                       for index in range(len(self.counter_locations)):
                           
                           if(self.counter_locations[index][1].\
                              get_center().to_frac() == coordinates):
                               self.counter_locations[index] = \
                                                             (player,
                                                              self.counter_locations[index][1])
                               break                   

    def any_valid_moves(self : 'CounterPositons', turn_player : str) -> str:
        '''
        This member function checks if there are any valid moves for a
        particular player on the board.
        '''
        truth_tuple = self.gameboard.any_valid_moves(turn_player[0])
        return truth_tuple[0]
    
    def place_counter(self : 'CounterPositions', x : int, y : int, width : int,
                      height : int, player : str) -> bool:
        '''
        This member function tries to place a counter on the board during
        gameplay. If it is an invalid move, the function will return false.
        Otherwise, it is recorded into the Othello object and returns true.
        '''
        temp_point = othello_point.from_pixel(x, y, width, height)

        for row_index in range(len(self.spot_coordinates)):
            for column_index in range(len(self.spot_coordinates[row_index])):
                
                if (self.spot_coordinates[row_index][column_index].\
                    inside_circle(temp_point)):

                    if(self.initial_setup[row_index][column_index] == '.'):
                        
                        placement = self.gameboard.player_turn(row_index,
                                                               column_index,
                                                               player)

                        if (placement):
                            self.counter_locations.append(
                                (player,
                                 self.spot_coordinates[row_index][column_index]))
                            self.flip_counters(player)

                        return placement

    def count(self : 'CounterPositions', player : str) -> int:
        '''
        This function returns the number of counters a player has on the board.
        It encapsulates the _counter_count function from the othello board.
        '''
        return self.gameboard._counter_count(player)
        
    def game_over(self : 'CounterPositions') -> bool:
        '''
        This member function returns whether or not the game is over or if it
        can continue.
        '''
        return not self.gameboard.any_valid_moves('B')[0] and\
               not self.gameboard.any_valid_moves('W')[0]\
               or self.gameboard.game_over()

    def calculate_winner(self : 'CounterPositions') -> str:
        '''
        This member function returns a string indicating who won based on the
        win condition. It encapsulates the calculate_winner function from the
        Othello object.
        '''
        return self.gameboard.calculate_winner()
    
                        
        
                    

