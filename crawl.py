import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(country, tab):
    # driver = webdriver.Chrome("chromedriver_win32/chromedriver") ###### ubuntu nhà tôi chạy Firefox nên các gs pull về đổi chrome cũng được nhé
    driver = webdriver.Firefox()
    URL = "https://www.chiasenhac.vn/mp3/" + country + ".html?tab=" + tab
    arr = np.arange(1, 20)

    save_path = 'data/'


    for i in arr:
        driver.get(URL + "&page=" + str(i))
        main = driver.find_elements_by_class_name('bai-hat-moi')
        print(main)

if __name__ == "__main__":
    country = input()
    tab = input()
    crawl(country, tab)

