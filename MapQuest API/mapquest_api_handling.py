'''
Name: Vincent Ha
Student ID: 14788488
'''
# mapquest_api_handling
# This module deals with the Mapquest API directly. It handles the JSON objects
# obtained directly from the API and changes them into a dictionary that is
# easier to deal.

import urllib.request
import urllib.parse
import json

MAPQUEST_API_KEY = 'SrFP4Wbx7c6E7p4qf7iYGRNzKPcAWudV'

MAPQUEST_BASE_URL = 'http://open.mapquestapi.com/'

def find_directions_query(starting_point : str, end_points : [str]) -> str:
    '''
    This function creates the url to utlize the Mapquest Directions API. It
    uses the urllib.parse.urlencode function to help create the necessary url.
    '''
    end_point_parameters = []
    for end_point in end_points:
        end_point_parameters.append(('to', end_point))
    
    direction_parameters = [('key', MAPQUEST_API_KEY),
                            ('from', starting_point)] + end_point_parameters

    return MAPQUEST_BASE_URL + 'directions/v2/route?' + urllib.parse.urlencode(
        direction_parameters)
    
def find_elevation_query(lat_list : [str], long_list : [str]) -> [str]:
    '''
    This function creates the url needed to use the Mapquest Elevations API.
    This function works similar to the function above.
    '''
    elevation_urls = []
     
    for index in range(len(lat_list)):
        elevation_parameters = [('key', MAPQUEST_API_KEY),
                                ('latLngCollection', str(lat_list[index]) + ','
                                + str(long_list[index])), ('unit', 'f')]
        elevation_urls.append(MAPQUEST_BASE_URL + 'elevation/v1/profile?'
                              + urllib.parse.urlencode(elevation_parameters))
    
    return elevation_urls

def get_info(url : str) -> dict:
    '''
    This function grabs the JSON obtained from the url provided and creates a
    dictionary that can be further processed another module.
    '''
    try:
        website = urllib.request.urlopen(url)
        json_text = website.read().decode(encoding = 'utf-8')
        info = json.loads(json_text)
        return info
    finally:
        if website != None:
            website.close()
