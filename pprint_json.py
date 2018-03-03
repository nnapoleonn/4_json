import json

import sys


def load_data(filepath):
    with open(filepath) as from_json:
        return json.loads(from_json.read())


def pretty_print_json(new_data):
    print(json.dumps(new_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))