import argparse
import logging
import subprocess

from typing import Tuple


def solution(file: str, hosts_file: str, log: logging.Logger) -> None:
    try:
        with open(hosts_file, "r") as hostsfile:
            hosts = hostsfile.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error reading from {hosts_file}: {exception}")
    else:
        for host in hosts:
            try:
                user, server = host.split(",")[0], host.split(",")[1]
                subprocess.run(["scp", f"{user}@{server}:{file}", f"./{user}_{server}_{file}"])
            except OSError as exception:
                log.error(f"Error copying file from {host}: {exception}")
                continue


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_14.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Get a file from a list of remote machines")
    parser.add_argument("-file", type=str, required=True,
                        help="Path of file to fetch")
    parser.add_argument("-hosts", type=str, default="hosts.txt",
                        help="File containing list of hosts")
    args = parser.parse_args()
    return args.file, args.hosts


def main():
    file, target_hosts = parse_args()
    log = setup_logging()
    solution(file, target_hosts, log)


if __name__ == '__main__':
    main()