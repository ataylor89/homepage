import json
import sys
import os

def create_dictionary(subjects):
    project_root = sys.path[0]
    path = f'{project_root}/homepage/static/data/dictionary/dictionary.json'
    if os.path.isfile(path):
        with open(path, 'r') as file:
            data = json.load(file)
            data['entries'] = [entry for entry in data['entries'] if set(subjects) & set(entry['subjects'])]
            return data
