import json
import yaml


def parsing(file_path):
	with open(file_path) as file:
		if file_path.endswith(".json"):
			return json.load(file)
		if file_path.endswith(".yaml") or file_path.endswith(".yml"):
			return yaml.load(file, Loader=yaml.FullLoader) or {}
		raise ValueError("Invalid file format")