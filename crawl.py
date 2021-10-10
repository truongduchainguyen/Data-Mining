import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(country, tab):
    driver = webdriver.Chrome("chromedriver_win32/chromedriver")
    URL = "https://www.chiasenhac.vn/mp3/" + country + "?tab=" + tab + "&page=1"
    driver.get(URL)

if __name__ == "__main__":
    country = input()
    tab = input()
    crawl(country, tab)
