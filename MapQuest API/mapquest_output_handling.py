'''
Name: Vincent Ha
Student ID: 14788488
'''

import mapquest_api_handling
import math

# Custom Exceptions
# ******************************************************************************
class InvalidPrintWorkError(Exception):
    '''
    This exception is triggered when the print function from the Route class
    detects a print job that is unknown to it.
    '''
    pass

class InvalidRouteError(Exception):
    '''
    This exception is triggered when a route is not found by the Mapquest API.
    This is distinguished from a MapquestError by seeing what particular error
    message is given from the JSON object returned by the Mapquest API.
    '''
    pass

class MapquestError(Exception):
    '''
    This exception is thrown when the Mapquest API has some sort of error. It is
    differentiated from the InvalidRouteError from the error message that is
    read from the JSON object read from API.
    '''
    pass

# Information Classes

# These classes are ones that hold each individual piece of route information.
# They all share the __str__ function, which returns a specific string when
# str() is called. This is important when calling the print function to print
# the information.
# ******************************************************************************

class Route_Steps:
    '''
    This class holds the directions from some starting point to some end
    point(s)
    '''
    def __init__(self : 'Route_Steps', direction_steps : [str]) -> 'Route_Steps':
        '''
        Constructor for the Route_Steps class. It takes a list of directions.
        '''
        self.direction_steps = direction_steps

    def __str__(self : 'Route_Steps') -> str:
        '''
        The shared function overload for all "information" classes. This one
        returns a string of directions in the wanted format.
        '''
        direction_str = 'DIRECTIONS\n'
        for direction in self.direction_steps:
            direction_str += direction + '\n'

        return direction_str

class Route_Travel_Time:
    '''
    This class holds the total travel time it takes to get from the starting
    point to the end point(s).
    '''
    def __init__(self : 'Route_Travel_Time',
                 total_travel_time : int) -> 'Route_Travel_Time':
        '''
        Constructor for the Route_Travel_Time class. It takes an integer
        representing a time in seconds.
        '''
        self.total_travel_time = total_travel_time/60

    def __str__(self : 'Route_Steps') -> str:
        '''
        The shared function overload for all "information" classes. This one
        returns a single-lined string with the time in integer form.
        '''
        return 'TOTAL TIME: {0:.0f} minutes\n'.format(self.total_travel_time)

class Route_Travel_Distance:
    '''
    This class holds the distance it takes to get from a starting point to the
    end point(s).
    '''
    def __init__(self : 'Route_Travel_Distance',
                 total_travel_distance : float) -> 'Route_Travel_Distance':
        '''
        The constructor for the Route_Travel_Distance class. This constructor
        takes a float that represents the route distance.
        '''
        self.total_travel_distance = total_travel_distance

    def __str__(self : 'Route_Travel_Distance') -> str:
        '''
        The shared function overload for all "information" classes. This one
        returns a singled-lined string with the distance written in integer form.
        '''
        return 'TOTAL DISTANCE: {0:.0f} miles\n'.format(
            self.total_travel_distance)

class Route_LatLongs:
    '''
    This class holds the coordinates of the starting point and end point(s)
    within the route. The coordinates are stored in a list of latitudes and a
    list of longitudes. These lists are both comprised of floats.
    '''
    def __init__(self : 'Route_LatLongs', latitudes : [float],
                 longitudes : [float]) -> 'Route_LatLongs':
        '''
        The constructor for the Route_LatLongs class. It takes two lists of
        floats, both represent the coordinates of points of interest.
        '''
        self.latitudes = latitudes
        self.longitudes = longitudes

    def __str__(self : 'Route_LatLongs') -> str:
        '''
        The shared function overload for all "information" classes. This one
        returns a string of coordinates in the wanted format. The format of the
        latitudes/longitudes is that of a positive two decimal float followed by
        a compass direction.
        '''
        coordinate_str = 'LATLONGS\n'
        for index in range(len(self.latitudes)):
            # Sets the string for a latitude
            if self.latitudes[index] < 0 : 
                coordinate_str += '{0:.2f} S '.format(math.fabs(
                    self.latitudes[index]))
            else:
                coordinate_str += '{0:.2f} N '.format(
                    math.fabs(self.latitudes[index]))

            # Sets the string for a longitude
            if self.longitudes[index] < 0 : 
                coordinate_str += '{0:.2f} W\n'.format(math.fabs(
                    self.longitudes[index]))
            else:
                coordinate_str += '{0:.2f} E\n'.format(math.fabs(
                    self.longitudes[index]))

        return coordinate_str

class Route_Elevations:
    '''
    This class holds the elevations of the starting point and end point(s) of a
    given route. The elevations are held as a list of floats.
    '''
    def __init__(self : 'Route_Elevations',
                 elevations : [float]) -> 'Route_Elevations':
        '''
        The constructor for the Route_Elevations class. This constructor takes
        one list of floats representing elevations in feet above sea level.
        '''
        self.elevations = elevations

    def __str__(self : 'Route_Elevations') -> str:
        '''
        The shared function overload for all "information" classes. This one
        returns a string of elevations in the wanted format. The elevations are
        listed on their own line and represented in integer form.
        '''
        elevation_str = 'ELEVATIONS\n'
        for height in self.elevations:
            elevation_str += '{0:.0f}\n'.format(height)

        return elevation_str

# Route Class
# ******************************************************************************

class Route:
    '''
    The Route class holds the information that the user may need to know about
    the specific route the user specified. The class prints the information
    based on what the user wants printed.
    '''
    def __init__(self : 'Route', direction_steps : 'Route_Steps',
                 total_travel_time : 'Route_Travel_Time',
                 total_travel_distance : 'Route_Travel_Distance',
                 latlongs : 'Route_LatLongs',
                 elevations : 'Route_Elevations') -> 'Route':
        '''
        Constructor for the Route class. It sets all the information that the
        user may need to see. Each piece of information is held within its own
        specialized class, with an overloaded __str__ function used for printing
        information out. A dictionary is set up in order to allow an ease of
        printing in the print function.
        '''
        self.direction_steps = direction_steps
        self.total_travel_time = total_travel_time
        self.total_travel_distance = total_travel_distance
        self.latlongs = latlongs
        self.elevations = elevations

        self.print_job_dictionary = {
            'LATLONG' : self.latlongs,
            'STEPS' : self.direction_steps,
            'TOTALTIME' : self.total_travel_time,
            'TOTALDISTANCE' : self.total_travel_distance,
            'ELEVATION' : self.elevations }
        
    def print(self, printing_list : [str]) -> None:
        '''
        This class member function prints information that the user is looking
        for based on what they have typed into the console. If there is a
        printing job that is unknown, this function rauses an exception.
        '''
        print()
        for print_work in printing_list:
            try:
                print(self.print_job_dictionary[print_work])
            except KeyError:
                raise InvalidPrintWorkError
            
        print('Directions Courtesy of MapQuest; Map Data Copyright' +
              ' OpenStreetMap Contributors')

# Functions
# ******************************************************************************

def _sort_direction_info(direction_dict : dict) -> ([str], int, float, [str],
                                                    [str]):
    '''
    This function sorts the information given from the directions API. It grabs
    the directions, coordinates, total distance traveled, and total time
    duration of the route from the dictionary taken from the website the API
    returns.
    '''
    if not direction_dict['route']['routeError']['message'] == '' or direction_dict['route']['routeError']['errorCode'] > 0:
        if direction_dict['info']['messages'][0] == 'We are unable to route with the given locations.':
            raise InvalidRouteError
        else:
            raise MapquestError
    
    dir_list = []
    lat_list = []
    long_list = []
    
    for step in direction_dict['route']['legs'][0]['maneuvers']:
        dir_list.append(step['narrative'])
    for location in direction_dict['route']['locations']:
        long_list.append(location['latLng']['lng'])
        lat_list.append(location['latLng']['lat'])
            
    directions_list = dir_list[:-1]
    total_time = direction_dict['route']['time']
    total_distance = direction_dict['route']['distance']
    return (directions_list, total_time, total_distance, lat_list, long_list)

def _sort_elevation_info(elevation_dict : [dict]) -> [str]:
    '''
    This function grabs the elevation levels of the locations specified by the
    user. This function uses the dictionary obtained from the JSON gained from
    the elevations API.
    '''
    elevation_list = []

    for profile in elevation_dict:
        for location in profile['elevationProfile']:
            elevation_list.append(location['height'])

    return elevation_list

def _get_route_info(starting_point : str, end_points : [str]) -> (list, int,
                                                                 float, list,
                                                                 list, list):
    '''
    This function grabs all the information the user may need and stores
    them in a tuple. This function uses the functions above to do this.
    '''
    direction_url = mapquest_api_handling.find_directions_query(starting_point,
                                                                end_points)
    direction_info_dict = mapquest_api_handling.get_info(direction_url)
    direction_info = _sort_direction_info(direction_info_dict)

    elevation_urls = mapquest_api_handling.find_elevation_query(direction_info[3],
                                                               direction_info[4])

    elevation_dicts = []
    
    for url in elevation_urls:
        elevation_dicts.append(mapquest_api_handling.get_info(url))
    elevation_info = _sort_elevation_info(elevation_dicts)
    
    return direction_info + (elevation_info,)   

def get_route(starting_point : str, end_points : [str]) -> 'Route':
    '''
    This function obtains all the information that may be necessary for the user
    and stores them first, in their own classes, then in a Route class.
    The information is stored in their individual classes to allow for the ease
    of printing. The Route class created in this functionis then returned at the
    end of the function. 
    '''
    info_tuple = _get_route_info(starting_point, end_points)

    route_info = Route(Route_Steps(info_tuple[0]),
                       Route_Travel_Time(info_tuple[1]),
                       Route_Travel_Distance(info_tuple[2]),
                       Route_LatLongs(info_tuple[3], info_tuple[4]),
                       Route_Elevations(info_tuple[5]))

    return route_info


