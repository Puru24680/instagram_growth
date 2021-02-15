from instapy import InstaPy
from config import password
from selenium import webdriver
diver = webdriver.Chrome()


session = InstaPy(username="69_fucks_", password=password,headless_browser=True)
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)