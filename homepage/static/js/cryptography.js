class Cryptography {

    constructor() {
        this.addEventListeners();
    }

    addEventListeners() {
        $('#algorithm').on('change', this.handleAlgorithmChange);
        $('#input').on('input', this.handleTextInput);
        $('#cryptography').on('submit', this.handleFormSubmission);
    }

    handleAlgorithmChange() {
        let value = $('#algorithm').val();
        if (value == 'RSA' || value == 'XOR') {
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
