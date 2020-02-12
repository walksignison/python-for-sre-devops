import logging
import argparse

from typing import Tuple


def solution(infile: str, limit: int, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as input:
            input_lines = input.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening input file: {exception}")
    else:
        output_lines = input_lines.reverse()
        if limit:
            output_lines = input_lines[:limit]
        try:
            with open(f"{infile}_reversed", "w") as out_file:
                for out_line in output_lines:
                    out_file.write(out_line[::-1]+"\n")
        except (IOError, FileNotFoundError) as exception:
            log.error(f"Error opening output file: {exception}")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_05.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, int]:
    parser = argparse.ArgumentParser(description="Reverse content of a file")
    parser.add_argument("-infile", type=str, required=True,
                        help="Filename of file to reverse")
    parser.add_argument("-limit", type=int, default=None,
                        help="Limit on number of lines to reverse")
    args = parser.parse_args()
    return args.infile, args.limit


def main():
    in_file, limit = parse_args()
    log = setup_logging()
    solution(in_file, limit, log)


if __name__ == '__main__':
    main()