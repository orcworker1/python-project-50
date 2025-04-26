import json
from pathlib import Path


def parse_file(file):
    with open(file, 'r') as f:
        return json.load(f)
    

def give_data(f_path):
    path = Path(f_path)
    if str(path).endswith('.json'):
        return parse_file(path)
    



