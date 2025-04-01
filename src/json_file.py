import json


def read_json(path: str):
    f = open(path, encoding="UTF8")
    data = json.load(f)
    f.close()
    return data


def save_json(data, file_path: str):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)


def string_json_to_dict(content: str):
    return json.loads(content)
