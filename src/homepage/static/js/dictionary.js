class Dictionary {
    
    constructor() {
        this.addEventListeners();
    }

    addEventListeners() {
        $('#dictionary_form').on('submit', this.handleSubmit);
    }

    handleSubmit(e) {
        e.preventDefault();
        $.post('/api/dictionary/create', $('#dictionary_form').serialize(), function(data) {
            $('#dictionary tbody').empty();
            for (let i = 0; i < data.entries.length; i++) {
                let entry = data.entries[i];
                let wordOrPhrase = entry.entry;
                let definitions = []
                if (entry.definitions.length == 1) {
                    definitions.push(entry.definitions[0]);
                }
                else if (entry.definitions.length > 1) {
                    for (let j = 0; j < entry.definitions.length; j++) {
                        if (entry.definitions[j]) {
                            let index = j + 1;
                            definitions.push('(' + index + ') ' + entry.definitions[j]);
                        }
                    }
                }
                let definition = definitions.join(' ');
                let tr = $('<tr/>');
                let td0 = $('<td/>').html(wordOrPhrase);
                let td1 = $('<td/>').html(definition);
                tr.append(td0);
                tr.append(td1);
                $('#dictionary tbody').append(tr);
            }
            $('#dictionary').show();
        });
    }
}

$(document).ready(function() {
    new Dictionary();
});
