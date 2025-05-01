def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower() 
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{'    ' * (depth + 1)}{k}: "
                         f"{format_value(v, depth + 1)}")
        return ('{\n' + '\n'.join(lines) + '\n' + '    '
                * depth + '}')
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, depth=0):
    lines = []

    def value_formatter(v):
        return format_value(v, depth + 1)
    for key, node in diff.items():
        indent = '    ' * depth
        if node['type'] == 'nested':
            lines.append(
                f"{indent}    {key}: {format_stylish(node['children'],
                                                     depth + 1)}"
            )
        elif node['type'] == 'added':
            lines.append(
                f"{indent}  + {key}: {value_formatter(node['value'])}"
            )
        elif node['type'] == 'removed':
            lines.append(
                f"{indent}  - {key}: {value_formatter(node['value'])}"
            )
        elif node['type'] == 'changed':
            lines.append(
                f"{indent}  - {key}: {value_formatter(node['old'])}"
            )
            lines.append(
                f"{indent}  + {key}: {value_formatter(node['new'])}"
            )
        else:
            lines.append(
                f"{indent}    {key}: {value_formatter(node['value'])}"
            )
    result = '\n'.join(lines)
    closing_indent = '    ' * depth
    return f'{{\n{result}\n{closing_indent}}}' if depth else f'{{\n{result}\n}}'
