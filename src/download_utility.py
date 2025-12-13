import requests
from pathlib import Path

def url_is_working(url: str) -> bool:
    """
    Check whether a URL is reachable and returns a successful HTTP response.

    The function sends an HTTP GET request to the given URL and considers it
    working if the response status code is in the 200–399 range. Network
    errors, timeouts, or unexpected status codes will result in False.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is reachable and responds successfully,
              False otherwise.
    """
    try:
        response = requests.get(url, timeout=5)
        assert 200 <= response.status_code < 400
        return True
    except Exception:
        return False

def file_exists(path: str) -> bool:
    """
    Check whether a file exists at the given path.

    The function returns True only if the path exists and refers to a regular
    file (not a directory).

    Args:
        path (str): The file system path to check.

    Returns:
        bool: True if the file exists and is a file,
              False otherwise.
    """
    return Path(path).is_file()
