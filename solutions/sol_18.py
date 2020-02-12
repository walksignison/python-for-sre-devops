import logging
import re


def parse_logs(logs: list) -> None:
    for log in logs:
        lines = log.split(" ")
        host = lines[3]
        timestamp = [re.search(r"\d{2}:\d{2}:\d{2}", line).group(0) for line in lines
                     if re.search(r"\d{2}:\d{2}:\d{2}", line)][0]
        dest = [re.search(r"to=<.*>,", line).group(0) for line in lines
                       if re.search(r"to=<.*>,", line)]
        if len(dest) > 0:
            dest = dest[0][dest[0].find("<")+len("<"):dest[0].rfind(">")]
        else:
            dest = ""
        print(timestamp, host, dest)


def solution(log: logging.Logger) -> None:
    try:
        with open("file.log", "r") as logfile:
            logs = logfile.read().splitlines()
    except (IOError, FileNotFoundError) as exception:
        log.error(f"Error reading file: {exception}")
    else:
        parse_logs(logs)


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_18.log")
    logger.addHandler(file_handle)
    return logger


def main():
    log = setup_logging()
    solution(log)


if __name__ ==  '__main__':
    main()