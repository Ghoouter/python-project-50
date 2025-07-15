from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.parser_args import parser_args


def main():
	args = parser_args()
	print(generate_diff(args.first_file, args.second_file, args.format))

	if __name__ == '__main__':
		main()