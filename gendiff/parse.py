import json
from pathlib import Path


def parse_file(file):
    with open(file,'r') as f:
        return json.load(f)
    

def give_data(f_path):
    path = path(f_path)
    if path.endswitch('.json'):
        return parse_file(path)
    



