import json
import yaml
from pathlib import Path

def parse(content, format_name):
        if format_name == 'json':
            return json.loads(content)
        elif format_name in ('yaml', 'yml'):
            return yaml.safe_load(content)

def get_data(file_path):
    path = Path(file_path)
    with open(path) as f:
            content = f.read()
    if path.suffix == '.json':
        return parse(content, 'json')
    elif path.suffix in ('.yaml', '.yml'):
        return parse(content, 'yaml')



