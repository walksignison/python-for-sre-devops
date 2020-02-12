import os
import time
import logging
import argparse

REMOVE_THRESHOLD_DAYS = 30.0
ONE_DAY_IN_SECONDS = 86400


def solution(releases_to_keep: str, log: logging.Logger) -> None:
    os.chdir("/path/to/releases")
    try:
        files = sorted(os.walk('.').next()[1], key=os.path.getmtime)[:-int(releases_to_keep)]
    except OSError as exception:
        log.error(f"Error reading releases from release directory: {exception}")
    else:
        try:
            to_keep = [file for file in files if file not in {"current", os.readlink("current")}]
        except OSError as exception:
            log.error(f"Error reading current symlink: {exception}")
        else:
            for element in to_keep:
                if ((time.time() - os.path.getmtime(element))/ONE_DAY_IN_SECONDS) > REMOVE_THRESHOLD_DAYS:
                        os.rmdir(element)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_20.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Cleanup releases")
    parser.add_argument("-keep", type=int, default=3,
                        help="Number of most recent releases to keep")
    args = parser.parse_args()
    return args.keep


def main():
    releases_to_keep = parse_args()
    log = setup_logging()
    solution(releases_to_keep, log)


if __name__ ==  '__main__':
    main()