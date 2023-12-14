import json


def format_php_array(data, indent=0):
    php_array = '['
    if isinstance(data, dict):
        for i, (key, value) in enumerate(data.items()):
            php_array += '\n' + '    ' * (indent + 1)
            php_value = format_php_value(value, indent + 1)
            php_array += f"'{key}' => {php_value}"
            if i < len(data) - 1:
                php_array += ','
    elif isinstance(data, list):
        for i, item in enumerate(data):
            php_array += '\n' + '    ' * (indent + 1)
            php_value = format_php_value(item, indent + 1)
            php_array += php_value
            if i < len(data) - 1:
                php_array += ','
    else:
        return format_php_value(data, indent)
    php_array += '\n' + '    ' * indent + ']'
    return php_array


def format_php_value(value, indent):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, (dict, list)):
        return format_php_array(value, indent)
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


if __name__ == "__main__":
    json_data = json.load(open("./input.json", "r"))

    # 格式化PHP数组
    formatted_php_array = format_php_array(json_data)
    print("<?php\n$myArray = " + formatted_php_array + ";\n?>")
