import sys 
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from src.download_utility import url_is_working
from src.download_utility import file_exists

def test_url_is_working():
    url1 = 'http://bad.url.this.probably.should.not.work.org'
    assert url_is_working(url1) == False

    url2 = 'http://google.com'
    assert url_is_working(url2) == True

    url3 = 'h t t p : / / '
    assert url_is_working(url3) == False


def test_file_exists_relative_path():
    relative_path = Path("test") / "test_download_utility.py"
    assert file_exists(str(relative_path)) is True

    relative_path = Path("LICENSE")
    assert file_exists(str(relative_path)) is True

    relative_path = Path("LICENSES") / "test_download_utility.py"
    assert file_exists(str(relative_path)) is False