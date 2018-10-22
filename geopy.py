from geopy.exc import GeocoderTimedOut
from time import sleep
def do_geocode(address):
    geopy = Nominatim()
    try:
        return geopy.geocode(address)
    except GeocoderTimedOut:
        sleep(1)
        return do_geocode(address)


for index, row in penn_data.iterrows():
    try:
        #address_1 = row['Borough'] 
        #address_2 = address_1.split(',')[-1]
        #address = address_2+","+"___"
        address_1 = row['Borough'] 
        address = address_1+","+row['County']+","+"___"
        #print(address)
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        #location = do_geocode(address)
        latitude = location.latitude
        longitude = location.longitude
        #print(row['District'],address, latitude, longitude)
        n_hood = n_hood.append({'Latitude': latitude,'Longitude': longitude}, ignore_index=True)
        n_hood
        pass
    except ValueError as error_message:
        print("Error")
        pass
    except AttributeError:
        #print("Problem with data or cannot Geocode.")
        address = row['County']+","+"___"
        #print(address)
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        #location = do_geocode(address)
        latitude = location.latitude
        longitude = location.longitude
        #print(address, latitude, longitude)
        n_hood = n_hood.append({'Latitude': latitude,'Longitude': longitude}, ignore_index=True)
        #print(row['District'],address, latitude, longitude)
        n_hood
        pass
