from flask import request, render_template, jsonify
from homepage import app, weather, calendar, cryptography, dictionary
from algorithms.key_manager import key_names

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

@app.route('/cryptography', methods=['GET'])
def cryptography_view():
    return render_template('cryptography.html', keys=key_names)

@app.route('/cryptography_service', methods=['POST'])
def cryptography_service():
    algorithm = request.form['algorithm']
    key = request.form['key']
    message = request.form['input'].replace('\r\n', '\n')
    action = request.form['action']
    return cryptography.crypt(algorithm, key, message, action)

@app.route('/dictionary', methods=['GET'])
def dictionary_view():
    return render_template('dictionary.html')

@app.route('/create_dictionary', methods=['POST'])
def create_dictionary():
    subjects = request.form.getlist('subjects')
    return dictionary.create_dictionary(subjects)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
