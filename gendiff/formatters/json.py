import json

def format_json(diff):
    return json.dump(diff, indent=2, ensure_ascii=False)
