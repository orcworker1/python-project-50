def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{'    ' * (depth + 1)}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * depth + '}'
    return str(value)


def format_stylish(diff, depth=0):
    lines = []
    for item in diff:
        key = item['key']
        indent = '    ' * depth
        
        if item['type'] == 'nested':
            value = format_stylish(item['children'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif item['type'] == 'added':
            value = format_value(item['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif item['type'] == 'removed':
            value = format_value(item['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif item['type'] == 'changed':
            old_value = format_value(item['old_value'], depth + 1)
            new_value = format_value(item['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        else:
            value = format_value(item['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
    
    result = '\n'.join(lines)
    return '{\n' + result + '\n' + '    ' * depth + '}' if depth else '{\n' + result + '\n}'
