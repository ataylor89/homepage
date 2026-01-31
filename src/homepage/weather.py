import requests

def get_forecast(latitude, longitude):
    url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
    resp1 = requests.get(url1)
    url2 = resp1.json()['properties']['forecast']
    resp2 = requests.get(url2)
    data = resp2.json()['properties']
    forecast = parse_json_response(data)
    forecast['latitude'] = latitude
    forecast['longitude'] = longitude
    return forecast

def parse_json_response(data):
    forecast = {}
    forecast['elevation'] = format('%f m' %data['elevation']['value'])
    forecast['generatedAt'] = data['generatedAt']
    forecast['units'] = data['units']
    forecast['periods'] = []
    for src in data['periods']:
        target = {}
        target['name'] = src['name']
        target['temperature'] = str(src['temperature']) + ' ' + src['temperatureUnit']
        if src['probabilityOfPrecipitation']['value'] is None:
            target['probabilityOfPrecipitation'] = 'N/A'
        else:
            target['probabilityOfPrecipitation'] = str(src['probabilityOfPrecipitation']['value']) + '%'
        target['windDirection'] = src['windDirection']
        target['windSpeed'] = src['windSpeed']
        target['shortForecast'] = src['shortForecast']
        target['detailedForecast'] = src['detailedForecast']
        target['icon'] = src['icon']
        forecast['periods'].append(target)
    return forecast

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32
