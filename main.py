import requests, smtplib
from time import sleep 

#initials
iss_url = 'http://api.open-notify.org/iss-now.json'
sun_url = 'https://api.sunrise-sunset.org/json'
api_key = '8712096633a11db4d978938e6b263ed3'
url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}&units=metric'

### ISS Data ### 
iss_data = requests.get(iss_url).json()
position = {
	'latitude': iss_data['iss_position']['latitude'],
	'longitude': iss_data['iss_position']['longitude']
}

lat = position['latitude']
lng = position['longitude']

postition_info = requests.get(sun_url, params=position)
data = postition_info.json()

#Sunrise or Sunset Data
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(f'sunrise: {sunrise}\nsunset: {sunset}')

### Getting Weather Data
def weather_update():
    weather_response = requests.get(url.format(lat,lng,api_key)).json()
    current_weather = weather_response['current']
    final_data = {
        'Temperature': current_weather['temp'],
        'Feels Like': current_weather['feels_like'],
        'Humidity': current_weather['humidity'],
        'Wind Spead(mi/h) ': current_weather['wind_speed'] 
    }

    weather_info_file = open('info.txt','w') 
    weather_info_file.writelines(str(final_data))
    weather_info_file.writelines(f'Latitude: {lat}')
    weather_info_file.writelines(f'Longitude: {lng}')
    weather_info_file.close()

def fetch_main():
    with open('info.txt','r') as file:
    content = dict(file.readlines)
    current_weather = content['current']
    

# print(final_data)
# print(lat)
# print(lng)

# def last_updated():
#     time = 0
#     while True:
#         sleep(1)
#         print(f'Last Updated {time+1} seconds ago.')
#         time+=1
#         if time == 9:
#             break

# remaining = 945
# while remaining>0:
#     weather_update()
#     print('Remaining:',remaining)
#     last_updated()
#     remaining-=1
