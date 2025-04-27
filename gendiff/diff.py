from gendiff.parse import parse_file

def lower_format(value):
    if isinstance(value,bool):
        return str(value).lower()
    return str(value)


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        if key not in data2:
            diff.append({'key': key, 'type': 'removed', 'value': lower_format(data1[key])})
        elif key not in data1:
            diff.append({'key': key, 'type': 'added', 'value': lower_format(data2[key])})
        elif data1[key] == data2[key]:
            diff.append({'key': key, 'type': 'unchanged', 'value': lower_format(data1[key])})
        else:
            diff.append({'key': key, 'type': 'changed', 'old_value':
                          lower_format(data1[key]), 
                         'new_value': lower_format(data2[key])})
    
    return diff


def format_diff(diff):
    lines = []
    for item in diff:
        if item['type'] == 'removed':
            lines.append(f"  - {item['key']}: {item['value']}")
        elif item['type'] == 'added':
            lines.append(f"  + {item['key']}: {item['value']}")
        elif item['type'] == 'changed':
            lines.append(f"  - {item['key']}: {item['old_value']}")
            lines.append(f"  + {item['key']}: {item['new_value']}")
        else:
            lines.append(f"    {item['key']}: {item['value']}")
    return '{\n' + '\n'.join(lines) + '\n}'


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff)