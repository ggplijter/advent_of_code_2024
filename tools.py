from dotenv import load_dotenv
load_dotenv()
import os
import httpx
from pathlib import Path

# Set up headers with the session cookie
headers = {
    "Cookie": f"session={os.environ["SESSION_COOKIE"]}",
}

ROOT_DIR = Path(__file__).parent


def get_local_input(path):
    with open(path, "r") as f:
        data = f.read()
    return data


def dump_input(destination: str, data: str) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with open(destination, "w") as f:
        f.write(data)
    return data

# Fetch the input
def fetch_input(url: str) -> str | None:
    url_path = httpx.URL(url).path
    destination = ROOT_DIR / f"./{url_path}.txt"

    if destination.exists():
        print("file exists in local storage")
        return get_local_input(destination)

    try:
        with httpx.Client() as client:

            print(f"Fetching data from {url}")
            response = client.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

            return dump_input(destination, response.text.strip()) # Return the input as a string
    except httpx.HTTPStatusError as exc:
        print(f"Error fetching input: {exc}")
        return None


def dump_assignment(url_path: str, data: str) -> None:
    # ['', '2024', 'day', '2']
    _, _, day, num = url_path.split("/")

    fname = f"{day}_{int(num):02d}.html"
    with open(fname, "w") as f:
        f.write(data)



def fetch_assignment(url: str):
    url_path = httpx.URL(url).path
    try:
        with httpx.Client() as client:
            print(f"Fetching assignment data from {url}")
            response = client.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404)
            # print(response.text)
            dump_assignment(url_path, response.text)
            # return dump_input(url_path, response.text.strip())  # Return the input as a string
    except httpx.HTTPStatusError as exc:
        print(f"Error fetching input: {exc}")
        return None