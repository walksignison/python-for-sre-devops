import argparse
import logging

from typing import Tuple


def solution(infile: str, word: str, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as input:
            input_lines = input.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening input file: {exception}")
    else:
        matches = [line for line in input_lines if word.lower() in line.lower()]
        for match in matches:
            print(match)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_12.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Find lines containing word")
    parser.add_argument("-infile", type=str, required=True,
                        help="Filename to check word for")
    parser.add_argument("-word", type=str, required=True,
                        help="Word to match")
    args = parser.parse_args()
    return args.infile, args.word


def main():
    in_file, word = parse_args()
    log = setup_logging()
    solution(in_file, word, log)


if __name__ == '__main__':
    main()