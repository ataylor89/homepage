class Calendar {
    year;
    month;
    data;

    constructor() {
        let today = new Date();
        this.year = today.getFullYear();
        this.month = today.getMonth();
    }

    init() {
        let $t = this;
        $.post('/calendar_data', {year: $t.year}, function(data) {
            $t.data = data;
            $t.flip($t.year, $t.month);
        });
        this.addEventListeners();
    }

    addEventListeners() {
        let $t = this;
        $("#prev_btn").click(function() {
            $t.back();
        });
        $("#next_btn").click(function() {
            $t.forward();
        });
    }

    createCell(dayOfMonth, daysInMonth, description) {
        let td = $('<td/>');
        let wrapper = $('<div/>');
        let head = $('<div/>').addClass('head');
        let body = $('<div/>').addClass('body');
        if (dayOfMonth >= 1 && dayOfMonth <= daysInMonth) {
            head.html(dayOfMonth);
            body.html(description);
        }
        wrapper.append(head);
        wrapper.append(body);
        td.append(wrapper);
        return td;
    }

    back() {
        if (this.month == 0) {
            this.flip(this.year - 1, 11);
        }
        else {
            this.flip(this.year, this.month - 1);
        }
    }

    forward() {
        if (this.month == 11) {
            this.flip(this.year + 1, 0);
        }
        else {
            this.flip(this.year, this.month + 1);
        }
    }

    flip(year, month) {
        let $t = this;
        if (this.year != year) {
            $.post('/calendar_data', {year: year}, function(data) {
                if (data) {
                    $t.year = year;
                    $t.data = data;
                    $t.flip(year, month);
                }
            });
        }
        else {
            this.month = month;
            $('#calendar tbody').empty();
            let calendar = this.data.calendar.months[month];
            let daysInMonth = calendar.days;
            let offset = calendar.offset;
            let numRows = Math.ceil((daysInMonth + offset) / 7);
            let dayOfMonth = 1 - offset;
            for (let i = 0; i < numRows; i++) {
                let tr = $('<tr/>');
                for (let j = 0; j < 7; j++) {
                    let description = calendar.entries.hasOwnProperty(dayOfMonth) ? calendar.entries[dayOfMonth] : '&nbsp;';
                    let td = this.createCell(dayOfMonth, daysInMonth, description);
                    tr.append(td);
                    dayOfMonth++;
                }
                $('#calendar tbody').append(tr);
            }
            $('#calendar_hdr').html(calendar.month + ' ' + year);
            this.updateButtons();
        }
    }

    updateButtons() {
        if (this.month == 0 && this.year == this.data.metadata.min_year) {
            $('#prev_btn').prop('disabled', true);
        }
        else {
            $('#prev_btn').prop('disabled', false);
        }
        if (this.month == 11 && this.year == this.data.metadata.max_year) {
            $('#next_btn').prop('disabled', true);
        }
        else {
            $('#next_btn').prop('disabled', false);
        }
    }
}

$(document).ready(function() {
    let calendar = new Calendar();
    calendar.init();
});
