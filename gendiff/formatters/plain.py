def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def plain_format(diff_result: dict):

    def walk(node, path):
        result = ''
        for k, v in node.items():
            current_path = f"{path}{v['key']}"
            if v['operation'] == 'changed':
                old_val = plain_value(v['old'])
                new_val = plain_value(v['new'])
                result += f"Property '{current_path}' was updated. " \
                         f"From {old_val} to {new_val}\n"
            elif v['operation'] == 'removed':
                result += f"Property '{current_path}' was removed\n"
            elif v['operation'] == 'added':
                value = plain_value(v['value'])
                result += f"Property '{current_path}' was added with value: " \
                         f"{value}\n"
            elif v['operation'] == 'nested':
                result += walk(v['value'], current_path + '.') + '\n'
        return result[:-1]
    return walk(diff_result, '')