import json


def normalize_value(value):
	if isinstance(value, bool):
		return str(value).lower()
	return value


def generate_diff(file_path1, file_path2):
	file1 = json.load(open(file_path1))
	file2 = json.load(open(file_path2))

	file1 = {k: normalize_value(v) for k, v in file1.items()}
	file2 = {k: normalize_value(v) for k, v in file2.items()}

	common_keys = file1.keys() & file2.keys()
	only_file1 = file1.keys() - file2.keys()
	only_file2 = file2.keys() - file1.keys()

	sorted_set = sorted(common_keys | only_file1 | only_file2)
	result = []

	for key in sorted_set:
		if key in common_keys and file1[key] == file2[key]:
			result.append(f'  {key}: {file1[key]}')
		if key in common_keys and file1[key] != file2[key]:
			result.append(f'- {key}: {file1[key]}')
			result.append(f'+ {key}: {file2[key]}')
		if key in only_file1:
			result.append(f'- {key}: {file1[key]}')
		if key in only_file2:
			result.append(f'+ {key}: {file2[key]}')
	return '\n'.join(result)