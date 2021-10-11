import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(country, tab):
    driver = webdriver.Chrome("chromedriver_win32/chromedriver") ###### ubuntu nhà tôi chạy Firefox nên các gs pull về đổi chrome cũng được nhé
    # driver = webdriver.Firefox()
    URL = "https://www.chiasenhac.vn/mp3/" + country + ".html?tab=" + tab
    arr = np.arange(1, 20)

    save_path = 'data/'

    # link_list = np.empty(1, dtype=str)
    link_list = []

    for i in arr:
        driver.get(URL + "&page=" + str(i))
        main = driver.find_element_by_class_name('content-current')
        songs = main.find_elements_by_css_selector('.media.align-items-stretch.not')
        for song in songs:
            a = song.find_element_by_tag_name("a")
            link = a.get_attribute("href")
            print(link)
            link_list.append(link)

if __name__ == "__main__":
    country = input()
    tab = input()
    crawl(country, tab)

