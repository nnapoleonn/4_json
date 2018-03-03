import json

import sys


def load_data(filepath):
    with open(filepath) as object_for_read:
        return json.loads(object_for_read.read())


def pretty_print_json(data_from_json):
    print(json.dumps(data_from_json, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        data_for_print = load_data(sys.argv[1])
        pretty_print_json(data_for_print)
    except IndexError:
        print('Enter path to file.')
    except FileNotFoundError:
        print('File not found.')
    except json.decoder.JSONDecodeError:
        print('It is not JSON file.')