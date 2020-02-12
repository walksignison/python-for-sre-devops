import logging
import argparse


def solution(infile: str, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as input:
            input_lines = input.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening input file: {exception}")
    else:
        print(f"Number of lines in this file are: {len(input_lines)}")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_07.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Print line count of file")
    parser.add_argument("-infile", type=str, required=True,
                        help="Filename to count lines of")
    args = parser.parse_args()
    return args.infile


def main():
    in_file = parse_args()
    log = setup_logging()
    solution(in_file, log)


if __name__ == '__main__':
    main()