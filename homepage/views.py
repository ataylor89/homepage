from flask import request, render_template, jsonify
from homepage import app, weather

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather_forecast():
    return render_template('weather.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    param = request.form['search_param']
    if param == 'city':
        city = request.form['city']
        latitude, longitude = weather.geocode(city)
    else:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        city = weather.rev_geocode(latitude, longitude)
    forecast = weather.get_forecast(latitude, longitude)
    forecast['city'] = city
    forecast['latitude'] = latitude
    forecast['longitude'] = longitude
    return jsonify(forecast)
