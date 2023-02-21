from pprint import pprint
import requests 
import os

key = os.environ.get('WEATHER_KEY')
print(key)

url= 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter the city')
country = input('Enter the 2-letter country code: ')
location = f'{city}, {country}'


query = {'q': location, 'units': 'metric', 'appid': key}

data = requests.get(url, params=query).json()