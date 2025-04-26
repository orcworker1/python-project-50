import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first file,', help='Path to the first file')
    parser.add_argument('second file',help='Path to the first file')
    parser.add_argument(
        "-f", "--format",
        choices=["json", "stylish", "plain"],
    )
    return parse_args()
