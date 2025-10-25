import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='weather')

def get_forecast(latitude, longitude):
    url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
    resp1 = requests.get(url1)
    url2 = resp1.json()['properties']['forecast']
    resp2 = requests.get(url2)
    data = resp2.json()['properties']
    forecast = format_json(data)
    return forecast

def format_json(data):
    forecast = {}
    forecast['elevation'] = format('%f m' %data['elevation']['value'])
    forecast['generatedAt'] = data['generatedAt']
    forecast['units'] = data['units']
    forecast['periods'] = []
    for src in data['periods']:
        dst = {}
        dst['name'] = src['name']
        dst['temperature'] = str(src['temperature']) + ' ' + src['temperatureUnit']
        if src['probabilityOfPrecipitation']['value'] is None:
            dst['probabilityOfPrecipitation'] = 'N/A'
        else:
            dst['probabilityOfPrecipitation'] = str(src['probabilityOfPrecipitation']['value']) + '%'
        dst['windDirection'] = src['windDirection']
        dst['windSpeed'] = src['windSpeed']
        dst['shortForecast'] = src['shortForecast']
        dst['detailedForecast'] = src['detailedForecast']
        dst['icon'] = src['icon']
        forecast['periods'].append(dst)
    return forecast

def geocode(city):
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

def rev_geocode(latitude, longitude):
    location = geolocator.reverse(format('%s, %s' %(latitude, longitude)), language='en')
    if location.raw['addresstype'] == 'city':
        return location.raw['name']

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32
