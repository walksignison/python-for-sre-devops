import argparse
import logging
import subprocess

from typing import Tuple


def solution(infile: str, outfile: str, log: logging.Logger) -> None:
    try:
        cmd = f"cat {infile}"
        output = subprocess.check_output(cmd,
                                         shell=True,
                                         stderr=subprocess.STDOUT)
    except (OSError, subprocess.CalledProcessError) as exception:
        log.error(f"Error reading {infile}: {exception}")
    else:
        try:
            with open(outfile, "w") as out_file:
                out_file.write(str(output.decode()))
        except (IOError, FileNotFoundError) as exception:
            log.error(f"Error writing to {outfile}: {exception}")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_13.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Output contents of infile to outfile")
    parser.add_argument("-infile", type=str, required=True,
                        help="Input filename")
    parser.add_argument("-outfile", type=str, required=True,
                        help="Output filename")
    args = parser.parse_args()
    return args.infile, args.outfile


def main():
    in_file, out_file = parse_args()
    log = setup_logging()
    solution(in_file, out_file, log)


if __name__ == '__main__':
    main()