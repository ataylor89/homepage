class WeatherForecast {

    constructor() {
        let today = moment().format("YYYY-MM-DD");
        $("#today").html("Today is " + moment().format("dddd MMMM Do YYYY"));
        this.addEventListeners();
    }

    handleKeyEvent() {
        let param = $('input[name="search_param"]:checked').val();
        if (param == 'city') {
            let city = $('input[name="city"]').val();
            if (city.length > 0) {
                $('button[type="submit"]').prop('disabled', false);
            }
            else {
                $('button[type="submit"]').prop('disabled', true);
            }
        }
        else if (param == 'coordinates') {
            let latitude = $('input[name="latitude"]').val();
            let longitude = $('input[name="longitude"]').val();
            if (latitude.length > 0 && longitude.length > 0) {
                $('button[type="submit"]').prop('disabled', false);
            }
            else {
                $('button[type="submit"]').prop('disabled', true);
            }
        }
    }

    handleRadioEvent() {
        let val = $('input[name="search_param"]:checked').val();
        if (val == 'city') {
            $('#search_by_city').show();
            $('#search_by_coordinates').hide();
        } else {
            $('#search_by_city').hide();
            $('#search_by_coordinates').show();
        }
        handleKeyEvent();
    }

    handleSubmit(e) {
        e.preventDefault();
        $.post('/weather_data', $('#searchform').serialize(), function(data) {
            $('input[name="city"]').val(data['city']);
            $('input[name="latitude"]').val(data['latitude']);
            $('input[name="longitude"]').val(data['longitude']);
            $('#forecast tr:not(:first-child)').remove();
            for (let i = 0; i < data['periods'].length; i++) {
                let period = data['periods'][i];
                let tr = $('<tr/>');
                let td0 = $('<td/>');
                td0.html(period['name']);
                tr.append(td0);
                let td1 = $('<td/>');
                td1.html(period['temperature']);
                tr.append(td1);
                let td2 = $('<td/>');
                td2.html(period['probabilityOfPrecipitation']);
                tr.append(td2);
                let td3 = $('<td/>');
                td3.html(period['windSpeed']);
                tr.append(td3);
                let td4 = $('<td/>');
                td4.html(period['windDirection']);
                tr.append(td4);
                let td5 = $('<td/>');
                td5.html(period['shortForecast']);
                tr.append(td5);
                let td6 = $('<td/>');
                td6.html(period['detailedForecast']);
                tr.append(td6);
                let td7 = $('<td/>');
                td7.html('<img src="' + period['icon'] + '"/>');
                tr.append(td7);
                $('#forecast').append(tr);
            }
            $('#forecast').show();
        });
    }

    addEventListeners() {
        $('input[name="city"]').on('input', this.handleKeyEvent);
        $('input[name="latitude"]').on('input', this.handleKeyEvent);
        $('input[name="longitude"]').on('input', this.handleKeyEvent);
        $('input[name="search_param"]').on('change', this.handleRadioEvent);
        $("#searchform").on('submit', this.handleSubmit);
    }
}

$(document).ready(function() {
    new WeatherForecast();
});
