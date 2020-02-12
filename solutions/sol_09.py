import argparse
import logging
import re

from typing import Tuple


def solution(infile: str, pattern: str, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as input:
            input_lines = input.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening input file: {exception}")
    else:
        matches = [line for line in input_lines if re.search(pattern, line)]
        for match in matches:
            print(match)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_09.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Grep")
    parser.add_argument("-infile", type=str, required=True,
                        help="Filename to check")
    parser.add_argument("-pattern", type=str, required=True,
                        help="Regex pattern to match")
    args = parser.parse_args()
    return args.infile, args.pattern


def main():
    in_file, pattern = parse_args()
    log = setup_logging()
    solution(in_file, pattern, log)


if __name__ == '__main__':
    main()