from gendiff.cli import parse_args
from gendiff.parse import give_data

def generate_diff(file1_path, file2_path):
    data1 = give_data(file1_path)
    data2 = give_data(file2_path)
    return {'file1': data1, 'file2': data2}


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))
    


if __name__ == '__main__':
    main()