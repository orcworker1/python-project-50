from gendiff.parses import get_data
from gendiff.formatters.stylish import format_stylish as stylish
from gendiff.formatters import get_formatter


def lower_format(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def build_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in keys:
        if key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {'type': 'nested', 'children': build_diff(data1[key], data2[key])}
        elif data1[key] == data2[key]:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {'type': 'changed', 'old': data1[key], 'new': data2[key]}
    
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


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)