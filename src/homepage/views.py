from homepage import key_names
from flask import request, render_template, jsonify
from homepage import app, weather, calendar, cryptography, dictionary

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather_view():
    return render_template('weather.html')

@app.route('/calendar', methods=['GET'])
def calendar_view():
    return render_template('calendar.html')

@app.route('/cryptography', methods=['GET'])
def cryptography_view():
    return render_template('cryptography.html', keys=key_names)

@app.route('/dictionary', methods=['GET'])
def dictionary_view():
    return render_template('dictionary.html')

@app.route('/api/weather/data', methods=['GET', 'POST'])
def weather_data():
    params = request.args if request.method == 'GET' else request.form
    latitude = params['latitude']
    longitude = params['longitude']
    forecast = weather.get_forecast(latitude, longitude)
    return jsonify(forecast)

@app.route('/api/calendar/data', methods=['GET', 'POST'])
def calendar_data():
    params = request.args if request.method == 'GET' else request.form
    year = int(params['year'])
    return jsonify(calendar.get(year))

@app.route('/api/cryptography/convert', methods=['GET', 'POST'])
def cryptography_service():
    params = request.args if request.method == 'GET' else request.form
    algorithm = params['algorithm']
    key = params['key']
    message = params['input'].replace('\r\n', '\n')
    action = params['action']
    return cryptography.crypt(algorithm, key, message, action)

@app.route('/api/dictionary/create', methods=['GET', 'POST'])
def create_dictionary():
    params = request.args if request.method == 'GET' else request.form
    subjects = params.getlist('subjects')
    return dictionary.create_dictionary(subjects)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
