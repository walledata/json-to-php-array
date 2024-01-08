import json
import argparse
import sys


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


def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert JSON to PHP array.")
    parser.add_argument("input_file", nargs='?', default="./input.json",
                        help="Path to the input JSON file. Default is './input.json'")
    parser.add_argument("output_file", nargs='?', default=None,
                        help="Path to the output PHP file. If not provided, output will be printed to console.")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    try:
        with open(args.input_file, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        sys.exit(f"Error: The file '{args.input_file}' does not exist.")
    except json.JSONDecodeError:
        sys.exit(f"Error: The file '{args.input_file}' contains invalid JSON.")

    formatted_php_array = format_php_array(json_data)

    if args.output_file:
        with open(args.output_file, "w") as output_file:
            output_file.write("<?php\n$myArray = " + formatted_php_array + ";\n?>")
    else:
        print("<?php\n$myArray = " + formatted_php_array + ";\n?>")
