def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower() 
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{'    ' * (depth + 1)}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * depth + '}'
    if value is None:
        return 'null'
    return str(value)

def format_stylish(diff, depth=0):
    lines = []
    for key, node in diff.items():
        indent = '    ' * depth
        value_formatter = lambda v: format_value(v, depth + 1)
        
        if node['type'] == 'nested':
            lines.append(f"{indent}    {key}: {format_stylish(node['children'], depth + 1)}")
        elif node['type'] == 'added':
            lines.append(f"{indent}  + {key}: {value_formatter(node['value'])}")
        elif node['type'] == 'removed':
            lines.append(f"{indent}  - {key}: {value_formatter(node['value'])}")
        elif node['type'] == 'changed':
            lines.append(f"{indent}  - {key}: {value_formatter(node['old'])}")
            lines.append(f"{indent}  + {key}: {value_formatter(node['new'])}")
        else:
            lines.append(f"{indent}    {key}: {value_formatter(node['value'])}")
    
    result = '\n'.join(lines)
    return '{\n' + result + '\n' + '    ' * depth + '}' if depth else '{\n' + result + '\n}'