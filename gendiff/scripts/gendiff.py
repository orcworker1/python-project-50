from gendiff.cli import parse_args


def main():
    args = parse_args()

    return (f'Comparing {args.first_file} and {args.second_file}"')


if __name__ == '__main__':
    main()