from gendiff.formatters import get_formatter
from gendiff.parses import get_data


def lower_format(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def build_diff(data1, data2):
    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in keys:
        if key not in data2:
            diff.append({'type': 'removed', 'key': key, 'value': data1[key]})
        elif key not in data1:
            diff.append({'type': 'added', 'key': key, 'value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'type': 'nested',
                'key': key,
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({'type': 'unchanged', 'key': key, 'value': data1[key]})
        else:
            diff.append({
                'type': 'changed',
                'key': key,
                'old_value': data1[key],
                'new_value': data2[key]
            })
    
    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)