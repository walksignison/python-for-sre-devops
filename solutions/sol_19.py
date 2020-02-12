import os
import shutil
import logging


def solution(log: logging.Logger) -> None:
    try:
        os.makedirs("/tmp/course/foo/bar")
    except (OSError, IOError) as exception:
        log.error(f"Error making directory /tmp/course/foo/bar: {exception}")
    else:
        try:
            shutil.copytree("/tmp/course/foo", "/tmp/course/foo2")
        except (OSError, IOError) as exception:
            log.error(f"Error copying directory /tmp/course/foo: {exception}")
        else:
            shutil.rmtree("/tmp/course/foo")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_19.log")
    logger.addHandler(file_handle)
    return logger


def main():
    log = setup_logging()
    solution(log)


if __name__ ==  '__main__':
    main()