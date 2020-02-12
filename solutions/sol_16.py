import argparse
import logging

from typing import Tuple


def solution(filelist: str, text: str, log: logging.Logger) -> None:
    outfiles = []
    files = filelist.split(",")
    try:
        outfiles = [file for file in files if text in open(file).read()]
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening file: {exception}")
    finally:
        for outfile in outfiles:
            print(outfile)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_16.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Find files containing target text")
    parser.add_argument("-filelist", type=str, required=True,
                        help="List of files")
    parser.add_argument("-text", type=str, required=True,
                        help="Target text to check against input files")
    args = parser.parse_args()
    return args.filelist, args.text


def main():
    list_of_files, text = parse_args()
    log = setup_logging()
    solution(list_of_files, text, log)


if __name__ ==  '__main__':
    main()
