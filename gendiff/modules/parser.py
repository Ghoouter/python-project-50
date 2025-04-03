import json

import yaml


def parse(data, format: str):
    if format == 'json':
        return json.load(data)
    if format == 'yaml':
        return yaml.safe_load(data)