import requests
import time
import logging

logging.basicConfig(
    filename="healthcheck.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def load_urls(filename):
    with open(filename, "r") as file:
        urls = []

        for line in file:
            line = line.strip()

            if line:
                urls.append(line)

    return urls


def check_url(url):
    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        response_time = round((end - start) * 1000)

        print("-" * 40)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time} ms")
        print("Status: UP")
        logging.info(f"{url} is UP - Status {response.status_code} - {response_time} ms")

    except requests.RequestException:
        print("-" * 40)
        print(f"URL: {url}")
        print("Status: DOWN")
        logging.error(f"{url} is DOWN")


def main():
    print("URL Health Checker")
    print("=" * 40)

    urls = load_urls("urls.txt")

    for url in urls:
        check_url(url)


if __name__ == "__main__":
    main()