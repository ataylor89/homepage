from flask import request, render_template, jsonify
from homepage import app, weather, calendar

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather_view():
    return render_template('weather.html')

@app.route('/weather_data', methods=['POST'])
def weather_data():
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

@app.route('/calendar', methods=['GET'])
def calendar_view():
    return render_template('calendar.html')

@app.route('/calendar_data', methods=['POST'])
def calendar_data():
    year = int(request.form['year'])
    return jsonify(calendar.get(year))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
