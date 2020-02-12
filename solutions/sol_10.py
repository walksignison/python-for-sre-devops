import argparse
import logging


def solution_b(infile: str, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as in_file:
            for line in in_file:
                pass
            last_line = line
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening file: {exception}")
    else:
        print(f"Last line in file {infile} is {last_line}")


def solution_a(infile: str, log: logging.Logger) -> None:
    try:
        with open(infile, "r") as in_file:
            lines = in_file.readlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening file: {exception}")
    else:
        print(f"Last line in file {infile} is {lines[-1]}")


def solution(infile: str, log: logging.Logger) -> None:
    solution_a(infile, log)
    solution_b(infile, log)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_10.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Print last line of file")
    parser.add_argument("-infile", type=str, required=True,
                        help="Filename to get last line of")
    args = parser.parse_args()
    return args.infile


def main():
    in_file = parse_args()
    log = setup_logging()
    solution(in_file, log)


if __name__ == '__main__':
    main()