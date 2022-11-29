import pytest
from scrape import status_code
import os

def test_status_code():
    assert status_code('https://github.com/topic/python') == 200

def test_file():
    assert os.path.exists(r"C:\Users\lette\OneDrive\Desktop\Web Scraping\Request Libray\scrape.json")
    
