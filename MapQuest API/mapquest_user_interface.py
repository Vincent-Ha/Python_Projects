'''
Name: Vincent Ha
Student ID: 14788488
'''
# mapquest_user_interface
# This module handles the input from the user and prints the information that
# the user requests regarding the route the user has specified.

# WARNING: PROGRAM MAY RUN SLOW

import mapquest_api_handling
import mapquest_output_handling

def _get_start_and_end_points() -> (str, [str]):
    '''
    This function handles getting the starting point and destinations the user
    wants to get to. It checks for the appropriate number of the locations.
    '''
    num_of_locations = int(input())
    if num_of_locations < 2: # Can't have a route without at least a starting
                             # and an end point.
        print('ERROR. Number of locations cannot be less than 2.')
        return ('N/A',)
                
    end_points = [None] * (num_of_locations - 1)
    starting_point = input()
    for index in range(num_of_locations - 1):
        end_points[index] = input()

    return (starting_point, end_points)

def _get_print_work() -> [str]:
    '''
    This function gets what information the user wants to see printed, also
    called printing jobs. It also checks for the appropriate number of printing
    jobs.
    '''
    num_of_print_work = int(input())
    if num_of_print_work < 1: # Expecting at least one print job.
        print('ERROR. Input must be more than 0.')
        return []

    print_jobs = [None] * num_of_print_work
    for index in range(num_of_print_work):
        print_jobs[index] = input().upper()

    return print_jobs


def user_input() -> None:
    '''
    This function handles the input taken by the user and converts it into
    route information that will be printed. The user specifies what the starting
    point and destinations are. The function converts it into a route class
    to hold the information and prints information based on what the user wants.
    '''
    while(True):
        try:
            points_of_interest = _get_start_and_end_points()
            if (points_of_interest[0] == 'N/A'): # Means that the user input for
                continue                         # num_of_locations was invalid.
            
            route_info = mapquest_output_handling.get_route(points_of_interest[0],
                                                            points_of_interest[1]) 
        
            print_work = _get_print_work()
            if (len(print_work) == 0): # Means that the user input for the 
                continue               # number of print works was invalid.
            
            route_info.print(print_work)
            break
                
        except ValueError:
            print('ERROR. Input must be an integer.')
            
        except mapquest_output_handling.InvalidPrintWorkError:
            print('ERROR. Invalid print job.')
            
        except mapquest_output_handling.InvalidRouteError:
            print('NO ROUTE FOUND')

        except mapquest_output_handling.MapquestError:
            print('MAPQUEST ERROR')


if __name__ == '__main__':
    user_input()
