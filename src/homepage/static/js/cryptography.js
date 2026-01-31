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
        let className = '.' + value.toLowerCase();
        if (value == 'rsa' || value == 'xor') {
            $('#key').empty();
            for (let i = 0; i < _keys[value].length; i++) {
                let key = _keys[value][i];
                let option = $('<option/>').html(key).val(key);
                $('#key').append(option);
            }
        }
        $('div.form-group').filter(className).show();
        $('div.form-group').not('.all').not(className).hide();
    }

    handleTextInput() {
        let text = $('#input').val();
        $('button[type="submit"]').prop('disabled', text.length == 0);
    }

    handleFormSubmission(e) {
        e.preventDefault();
        $.post('/api/cryptography/compute', $('#cryptography').serialize(), function(data) {
            $('#output').val(data)
        });
    }
}

$(document).ready(function() {
    new Cryptography();
});
