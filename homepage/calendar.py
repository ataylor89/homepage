from datetime import datetime

def current():
    now = datetime.now()
    return get(now.year)

def get(year):
    if year in calendars:
        return {
            'metadata': calendars['metadata'],
            'calendar': calendars[year]
        }

calendars = {
    'metadata': {
        'min_year': 2025,
        'max_year': 2025
    },
    2025: {
        'year': 2025,
        'leap_year': False,
        'months': [
            {
                'month': 1,
                'monthname': 'January',
                'days': 31,
                'offset': 3,
                'entries': {
                    1: 'New Year\'s Day'
                }
            },
            {
                'month': 2,
                'monthname': 'February',
                'days': 28,
                'offset': 6,
                'entries': {
                    14: 'Valentine\'s Day'
                }
            },
            {
                'month': 3,
                'monthname': 'March',
                'days': 31,
                'offset': 6,
                'entries': {
                    17: 'Saint Patrick\'s Day',
                    20: 'March Equinox'
                }
            },
            {
                'month': 4,
                'monthname': 'April',
                'days': 30,
                'offset': 2,
                'entries': {
                    20: 'Easter Sunday',
                    21: 'Easter Monday'
                }
            },
            {
                'month': 5,
                'monthname': 'May',
                'days': 31,
                'offset': 4,
                'entries': {
                    11: 'Mother\'s Day'
                }
            },
            {
                'month': 6,
                'monthname': 'June',
                'days': 30,
                'offset': 0,
                'entries': {
                    15: 'Father\'s Day',
                    19: 'Juneteenth',
                    21: 'June Solstice'
                }
            },
            {
                'month': 7,
                'monthname': 'July',
                'days': 31,
                'offset': 2,
                'entries': {}
            },
            {
                'month': 8,
                'monthname': 'August',
                'days': 31,
                'offset': 5,
                'entries': {}
            },
            {
                'month': 9,
                'monthname': 'September',
                'days': 30,
                'offset': 1,
                'entries': {
                    1: 'Labor Day',
                    22: 'September Equinox'
                }
            },
            {
                'month': 10,
                'monthname': 'October',
                'days': 31,
                'offset': 3,
                'entries': {
                    31: 'Halloween'
                }
            },
            {
                'month': 11,
                'monthname': 'November',
                'days': 30,
                'offset': 6,
                'entries': {
                    1: 'World Vegan Day',
                    13: 'World Kindness Day',
                    27: 'Thanksgiving Day'
                }
            },
            {
                'month': 12,
                'monthname': 'December',
                'days': 31,
                'offset': 1,
                'entries': {
                    14: 'Hannukah',
                    15: 'Hannukah',
                    16: 'Hannukah',
                    17: 'Hannukah',
                    18: 'Hannnukah',
                    19: 'Hannukah',
                    20: 'Hannukah',
                    21: 'Hannukah<br/>December Solstice',
                    22: 'Hannukah',
                    24: 'Christmas Eve',
                    25: 'Christmas Day',
                    31: 'New Year\'s Eve'
                }
            }
        ]
    }
}
