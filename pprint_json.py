import json

import sys


def load_data(filepath):
    with open(filepath) as data_from_json:
        return json.loads(data_from_json.read())


def pretty_print_json(data_from_json):
    print(json.dumps(data_from_json, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        data_in_file = load_data(sys.argv[1])
        pretty_print_json(data_in_file)
    except IndexError:
        print('Enter path to file.')
    except FileNotFoundError:
        print('File not found.')