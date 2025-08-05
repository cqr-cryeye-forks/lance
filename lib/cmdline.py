import argparse
import sys


def cmdLineParser():
    parser = argparse.ArgumentParser(description='lance. By b4zinga@outlook.com', usage='python lance.py')
    parser.add_argument(
        "--target",
        help="target url.",
    )
    parser.add_argument(
        "--output",
        help="output JSON file to save results.",
    )
    parser.add_argument(
        "--disable-col",
        help="Disable color in terminal.",
    )
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    return parser.parse_args()
