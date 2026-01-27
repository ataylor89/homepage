import json
import sys
import os

def get(year):
    project_root = sys.path[0]
    metadata_path = f'{project_root}/homepage/static/data/calendar/metadata.json'
    calendar_path = f'{project_root}/homepage/static/data/calendar/{year}.json'
    if os.path.isfile(metadata_path) and os.path.isfile(calendar_path):
        metadata_file = open(metadata_path, 'r')
        calendar_file = open(calendar_path, 'r')
        metadata = json.load(metadata_file)
        calendar = json.load(calendar_file)
        return {'metadata': metadata, 'calendar': calendar}
