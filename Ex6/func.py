import math
import zip_util
import csv


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance


def get_loc(user_input_cmd):
    zip_codes = zip_util.read_zip_all()
    res = zip_codes[user_input_cmd]
    lat_degrees = f"{int(res[1])}\xb0 {int((res[1] - int(res[1]))*60)}' {int((res[1] - int(res[1]))*60 - int((res[1] - int(res[1])))*3600)}\" N"
    lan_degrees = f"{int(res[2])}\xb0 {int((res[2] - int(res[2]))*60)}' {int((res[2] - int(res[2]))*60 - int((res[2] - int(res[2])))*3600)}\" W"
    return f'ZIP Code {res[0]} is in {res[3]},  {res[4]} {res[-1]} county \ncoordinates: ({ lat_degrees}, {lan_degrees})'


def get_dist(user_input_first_code, user_input_second_code):
    zip_codes = zip_util.read_zip_all()
    lat1 = zip_codes[user_input_first_code][1]
    lon1 = zip_codes[user_input_first_code][2]
    lat2 = zip_codes[user_input_second_code][1]
    lon2 = zip_codes[user_input_second_code][2]
    dist_res = round(haversine(lat1, lon1, lat2, lon2), 2)
    return f"The distance between {user_input_first_code} and {user_input_second_code} is {dist_res} miles"


def get_zip(user_input_city, user_input_state):
    list_zip_code = []
    with open('zip_codes_states.csv', 'r') as file:
        data = csv.reader(file)
        for d in data:
            if d[3] == user_input_city and d[4] == user_input_state:
                list_zip_code.append(d[1])
        return f"The following ZIP Code(s) found for {user_input_city}, {user_input_state}: {', '.join(list_zip_code)}"
