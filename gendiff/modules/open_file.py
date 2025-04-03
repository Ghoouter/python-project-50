from pathlib import Path


def open_file(path):
    extension = Path(path).suffix
    if extension == '.json':
        format = 'json'
        data = open(path)
    elif extension == '.yml' or extension == '.yaml':
        format = 'yaml'
        data = Path(path).read_text()
    return data, format