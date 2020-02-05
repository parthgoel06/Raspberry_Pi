import googlemaps
import pprint
import time

gmaps = googlemaps.Client(key = 'AIzaSyDVCEYkZqhHzB5WUAM8qLFAraOAp4_YZUQ')

def Hospital():
    places_result_hospital = gmaps.places_nearby(location = '28.647177,77.341185', open_now = True, keyword = 'hospital', type = 'hospital', rank_by = 'distance')
    for place in places_result_hospital['results']:
        my_place_id = place['place_id']
        my_fields = ['name','formatted_phone_number','vicinity']
        details = gmaps.place(place_id = my_place_id, fields = my_fields)
        if len(details['result']['formatted_phone_number'])>1:
            break
    print(f"Hospital Name = {details['result']['name']}")
    print(f"Phone Number = {details['result']['formatted_phone_number']}")
    print(f"Address = {details['result']['vicinity']}\n")

def Police():
    places_result_police = gmaps.places_nearby(location = '28.647177,77.341185', open_now = False, keyword = 'police station', type = 'police', rank_by = 'distance')
    for place in places_result_police['results']:
        my_place_id = place['place_id']
        my_fields = ['name','formatted_phone_number','vicinity']
        details = gmaps.place(place_id = my_place_id, fields = my_fields)
        if len(details['result']['formatted_phone_number'])>1:
            break
    print(f"Police Station Name = {details['result']['name']}")
    print(f"Phone Number = {details['result']['formatted_phone_number']}")
    print(f"Address = {details['result']['vicinity']}")  

def long_lat():
    return('28.647177,77.341185')