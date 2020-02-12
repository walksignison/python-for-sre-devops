import os
import logging
import requests
import argparse

from typing import Tuple

API_KEY = os.getenv("OWM_API_KEY", None)
URL = "http://api.openweathermap.org/data/2.5/weather"


def solution(zip_code: str, country: str, log: logging.Logger) -> None:
    if API_KEY is not None:
        try:
            response = requests.get(URL, params={"zip": f"{zip_code},{country}",
                                                 "APPID": API_KEY})
            if response.status_code != 200:
                log.error(f"Error making request to {URL}: {response.status_code}")
            else:
                print(response.json())
        except requests.exceptions.RequestException as exception:
            log.error(f"Error making request to {URL}: {exception}")
    else:
        log.error("OWM_API_KEY is not set")


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    file_handle = logging.FileHandler("sol_02.log")
    logger.addHandler(file_handle)
    return logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Display current weather information")
    parser.add_argument("-zip", type=int, required=True,
                        help="Zip code to get the weather for")
    parser.add_argument("-country", default="US", type=str,
                        help="County zip code belongs to, default is US")
    args = parser.parse_args()
    return args.zip, args.country


def main():
    zip, country = parse_args()
    log = setup_logging()
    solution(zip, country, log)


if __name__ == '__main__':
    main()