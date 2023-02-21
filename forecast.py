import os
import requests
from pprint import pprint
from datetime import datetime




key = os.environ.get('WEATHER_KEY')
query = { 'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}


url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)


list_of_forecast = data['list']

for forecast in list_of_forecast:
    temp = forecast['main'] ['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimesstamp(timestamp)
    print(f'At {forecast_date} the temperature will be {temp}F')

