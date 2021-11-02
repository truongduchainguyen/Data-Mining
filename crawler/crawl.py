import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib3
import os
import time
import requests

def create_link_file(list_link):
    textfile = open("list_song.txt", "w")
    for element in list_link:
        textfile.write(element + "\n")
    textfile.close()

# def open_link_file(filename):


def crawl(country, tab):
    # driver = webdriver.Chrome("chromedriver_win32/chromedriver") ###### ubuntu nhà tôi chạy Firefox nên các gs pull về đổi chrome cũng được nhé
    driver = webdriver.Firefox()
    URL = "https://www.chiasenhac.vn/mp3/" + country + ".html?tab=" + tab
    arr = np.arange(1, 20)
    save_path = 'data/'
    link_list = []
    req = urllib3.PoolManager()

    for i in arr:
        driver.get(URL + "&page=" + str(i))
        main = driver.find_element_by_class_name('content-current')
        songs = main.find_elements_by_css_selector('.media.align-items-stretch.not')
        for song in songs:
            a = song.find_element_by_tag_name("a")
            link = a.get_attribute("href")
            # print(link)
            link_list.append(link)

    driver.close()

    for i in link_list:
        driver.get(i)
        prepare = driver.find_element_by_id("pills-download-tab").click()
        download = prepare.find_element_by_class_name("download_item")
        print(download.text)

        # res = req.request('GET', i)
        # soup = bs(res.data, 'html.parser')



if __name__ == "__main__":
    country = input()
    tab = input()
    crawl(country, tab)

