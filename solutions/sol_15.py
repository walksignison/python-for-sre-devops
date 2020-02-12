import fileinput
import argparse
import logging


def solution(filelist: str, log: logging.Logger) -> None:
    string_to_replace = input("Enter string to be replaced: ")
    replacement_string = input("Enter replacement string: ")
    try:
        with open(filelist, "r") as list_of_files:
            files = list_of_files.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error opening file {filelist}: {exception}")
    else:
        for file in files:
            try:
                with fileinput.FileInput(file, inplace=True) as lines:
                    for line in lines:
                        print(line.replace(string_to_replace,
                                           replacement_string),
                                           end="")
            except FileNotFoundError as exception:
                log.error(f"File does not exist... skipping to next one: {exception}")
                continue


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_15.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Replace string in list of files")
    parser.add_argument("-filelist", type=str, required=True,
                        help="Filename containing L`list of files")
    args = parser.parse_args()
    return args.filelist


def main():
    list_of_files = parse_args()
    log = setup_logging()
    solution(list_of_files, log)


if __name__ ==  '__main__':
    main()