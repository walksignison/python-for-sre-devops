import subprocess
import argparse
import logging


def solution(count: str, log: logging.Logger) -> None:
    cmd = f"ping -c{count} www.google.com"
    try:
        output = subprocess.check_output(cmd.split()).splitlines()
    except (OSError, subprocess.CalledProcessError) as exception:
        log.error(f"Error running command: {cmd}: {exception}")
    else:
        parsed_output = output[-1].decode().split(" ")[3].split("/")
        min, mean, max, stddev = parsed_output[0], parsed_output[1], parsed_output[2], parsed_output[3]
        print(f"RTT_min: {min}ms\nRTT_mean: {mean}ms\nRTT_max: {max}ms\nRTT_stddev: {stddev}ms")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_17.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="google.com RTT stats")
    parser.add_argument("-count", type=str, default="5",
                        help="Number of packets to send")
    args = parser.parse_args()
    return args.count


def main():
    packet_count = parse_args()
    log = setup_logging()
    solution(packet_count, log)


if __name__ ==  '__main__':
    main()