#!/usr/bin/python3

import pprint
import requests
import time
import reverse_geocoder as rg

def main():
    url = "http://api.open-notify.org/iss-now.json"
    getRequest= requests.get(url)
    position= getRequest.json()
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(position['timestamp']))
    lat =position['iss_position']['latitude']
    lon=position['iss_position']['longitude']
    coords_tuple= (lat, lon)
    result = rg.search(coords_tuple)
    location =result[0]['name']
    print(result)
    
    print(f"THe ISS latitude is {lat}")
    print(f"THe ISS longitude is {lon}")
    print(f"This is the position as of {my_time}")
    
    location =result[0]['name']
    if result[0]['admin1'] != '':
        location2=result[0]['admin1']
        print(f"The ISS is over {location}, {location2}")
    else:
        print(f"The ISS is over {location}")





if __name__ == "__main__":
    main()          