import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(country, tab):
    # driver = webdriver.Chrome("chromedriver_win32/chromedriver") ###### ubuntu nhà tôi chạy Firefox nên các gs pull về đổi chrome cũng được nhé
    driver = webdriver.Firefox()
    URL = "https://www.chiasenhac.vn/mp3/" + country + ".html?tab=" + tab
    arr = np.arange(1, 20)

    save_path = 'data/'

    # link_list = np.empty(1, dtype=str)
    link_list = []

    for i in arr:
        driver.get(URL + "&page=" + str(i))
        main = driver.find_element_by_class_name('content-current')
        a = main.find_elements_by_tag_name("a")
        for j in a:
            link = j.get_attribute("href")
            link_list.append(link)
    print(link_list)

if __name__ == "__main__":
    country = input()
    tab = input()
    crawl(country, tab)

