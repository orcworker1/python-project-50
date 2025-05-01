def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, parent_key=''):
    lines = []
    for key, node in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        
        if node['type'] == 'nested':
            lines.append(format_plain(node['children'], 
                                      current_key))
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_key}'"
                         f" was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_key}'"
                         f" was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old'])
            new_value = format_value(node['new'])
            lines.append(
                f"Property '{current_key}' was updated."
                f" From {old_value} to {new_value}"
            )
    
    return '\n'.join(lines)