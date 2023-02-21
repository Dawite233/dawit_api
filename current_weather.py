from pprint import pprint
import requests 
import os

key = os.environ.get('WEATHER_KEY')
print(key)

url = f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={key}'
key = os.environ.get('WEATHER_KEY')



def main():
    location = get_location()
    weather_data, error + get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}C')

def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) !=2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()

    location = f'{city}, {country}'
    return location

def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'metric', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_stataus()
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text) # added for debugging
        return None, ex

def get_temp(weather_data):
    try:
        temp = weather data['main']['temp']
        return temp
    except KeyError:
        print('This data is not in the formal expected')
        return 'Unknown'

if __name__ == '__main__':
    main()



