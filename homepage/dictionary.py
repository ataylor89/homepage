import json
import os

def create_dictionary(subjects):
    path = 'homepage/static/data/dictionary/dictionary.json'
    if os.path.isfile(path):
        with open(path, 'r') as file:
            data = json.load(file)
            data['entries'] = [entry for entry in data['entries'] if set(subjects) & set(entry['subjects'])]
            return data
