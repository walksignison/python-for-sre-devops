import logging
import argparse
import subprocess


def solution(cmd: str, log: logging.Logger) -> None:
    try:
        process = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    except (OSError, ValueError) as exception:
        log.error(f"Error running command: {exception}")
    else:
        print(f"stdout: {stdout.decode()}, stderr: {stderr.decode()}")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_06.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Redirect stderr & stdout one way")
    parser.add_argument("-command", type=str, required=True,
                        help="Bash command to run")
    args = parser.parse_args()
    return args.command


def main():
    file = parse_args()
    log = setup_logging()
    solution(file, log)


if __name__ == '__main__':
    main()