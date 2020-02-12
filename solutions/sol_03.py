import sys
import socket
import logging
import argparse

from typing import Tuple


def solution(ip: str, port: str, log: logging.Logger) -> bool:
    sock = socket.socket()
    try:
        sock.connect((ip, int(port)))
    except socket.error as exception:
        log.error(f"Error while connecting to socket on {ip}:{port} - {exception}")
        return False
    else:
        return True


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_03.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Test connectivity to a socket")
    parser.add_argument("-ip", type=str, required=True,
                        help="IP address of socket to test")
    parser.add_argument("-port", type=str, required=True,
                        help="Port of socket to test")
    args = parser.parse_args()
    return args.ip, args.port


def main():
    ip, port = parse_args()
    log = setup_logging()
    if solution(ip, port, log):
        print(f"Successful connection to {ip}:{port}")
        sys.exit(0)
    else:
        sys.exit(f"Unsuccessful connection to {ip}:{port}")


if __name__ == '__main__':
    main()