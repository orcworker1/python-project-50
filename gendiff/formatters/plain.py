def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null' 
    elif isinstance(value, bool):
        return str(value).lower()  
    else:
        return str(value)


def format_plain(diff, path=''):
    lines = []
    for node in diff: 
        key = node.get('key')
        node_type = node.get('type')
        current_path = f"{path}.{key}" if path else key

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value:"
                         f" {value}")
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old_value} "
                f"to {new_value}"
            )
    return '\n'.join(lines)