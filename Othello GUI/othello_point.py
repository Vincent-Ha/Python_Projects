'''
Name : Vincent Ha
Student ID : 14788488
'''

import math

class Point:
    '''
    The Point class records the x and y coordinates of a point in a tkinter
    canvas board. It holds these values using ratios and can return them
    as is or by pixels. This class can also determine the distance from itself
    to another point.
    '''
    def __init__(self : 'Point', x_coord : float , y_coord : float) -> 'Point':
        '''
        The constructor for the Point class. It holds the x and y coordinates
        as ratios.
        '''
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

    def to_pixel(self : 'Point', width : float, height : float) -> (float,
                                                                    float):
        '''
        This member function returns the x and y coordinates as pixels based
        on the width and length.
        '''
        return (self.x_coordinate * width, self.y_coordinate * height)

    def to_frac(self : 'Point') -> (float, float):
        '''
        This member function returns the x and y coordinates as they are stored
        in the object.
        '''
        return (self.x_coordinate, self.y_coordinate)

    def distance_from_frac(self, p : 'Point') -> float:
        '''
        This member function returns the distance between this point and a
        point given to the function.
        '''
        return math.sqrt(
            ((self.x_coordinate - p.x_coordinate) *
             (self.x_coordinate - p.x_coordinate)) \
            + ((self.y_coordinate - p.y_coordinate) *
               (self.y_coordinate - p.y_coordinate)))       

    
def from_frac(x : float, y : float) -> 'Point':
    '''
    This function returns a Point object based on the input given.
    '''
    return Point(x,y)

def from_pixel(x : float, y : float, width : float, height : float) -> 'Point':
    '''
    This function converts the x and y positions into ratios that are used to
    create a Point object. This Point object is then returned.
    '''
    return Point(x / width, y / height)

