class Cryptography {

    constructor() {
        this.addEventListeners();
        this.handleAlgorithmChange();
    }

    addEventListeners() {
        $('#algorithm').on('change', this.handleAlgorithmChange);
        $('#input').on('input', this.handleTextInput);
        $('#cryptography').on('submit', this.handleFormSubmission);
    }

    handleAlgorithmChange() {
        let value = $('#algorithm').val();
        if (value == 'RSA') {
            $('#key').empty();
            for (let i = 0; i < _keys['RSA'].length; i++) {
                let key = _keys['RSA'][i];
                let option = $('<option/>').html(key).val(key);
                $('#key').append(option);
            }
            $('#key_selection').show();
        }
        else if (value == 'XOR') {
            $('#key').empty();
            for (let i = 0; i < _keys['XOR'].length; i++) {
                let key = _keys['XOR'][i];
                let option = $('<option/>').html(key).val(key);
                $('#key').append(option);
            }
            $('#key_selection').show();
        }
        else {
            $('#key_selection').hide();
        }
    }

    handleTextInput() {
        let text = $('#input').val();
        if (text.length > 0) {
            $('button[type="submit"]').prop('disabled', false);
        }
        else {
            $('button[type="submit"]').prop('disabled', true);
        }
    }

    handleFormSubmission(e) {
        e.preventDefault();
        $.post('/cryptography_service', $('#cryptography').serialize(), function(data) {
            $('#output').val(data)
        });
    }
}

$(document).ready(function() {
    new Cryptography();
});
