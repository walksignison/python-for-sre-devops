import argparse
import logging
import os


def solution(dir: str, log: logging.Logger) -> None:
    try:
        for dir_path, dir_names, file_names in os.walk(dir):
            for filename in file_names:
                filepath = os.path.join(dir_path, filename)
                filesize = os.path.getsize(filepath)
                print(f"{filepath}: {filesize} B")
    except OSError as exception:
        log.error(f"Error checking directory contents: {exception}")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_11.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Output size & contents of a directory")
    parser.add_argument("-directory", type=str, required=True,
                        help="Directory to view details of")
    args = parser.parse_args()
    return args.directory


def main():
    dir = parse_args()
    log = setup_logging()
    solution(dir, log)


if __name__ == '__main__':
    main()