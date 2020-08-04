import json


def print_json(j):
    print(json.dumps(j.json(), indent=2, ensure_ascii=False))