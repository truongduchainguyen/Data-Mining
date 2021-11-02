import os
import numpy as np
import pandas as pd
import requests
import re
import time
from bs4 import BeautifulSoup

def crawl(country, tab):
    URL = "https://www.chiasenhac.vn/mp3/" + country + ".html?tab=" + tab
    pages = np.arange(1,20)
    save_path='data/'
    link_list = []
    
    for page in pages:
        main = requests.get(URL+"&page="+str(page))
        songs = 
    
    pass

def crawlSong(initial_url, count=10, delay=3):
    url = initial_url
    
    for i in range(count):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # lấy Title và Artist
        name = soup.find(class_="d-flex justify-content-between mb-3 box1 music-listen-title")
        name = name.h1.text
        name = name.split(" - ")
        title = name[0]
        artist = name[1]
        
        # lấy link tải m4a và mp3
        download_div = soup.find(id="pills-download")
        download_items = download_div.find_all("a", class_="download_item", href=True)
        m4a_link = download_items[0]['href']
        mp3_link = download_items[1]['href']
                
        
        if title not in title_list or artist not in artist_list:
            title_list.append(title)
            artist_list.append(artist)
            link_list.append(url)
            m4a_list.append(m4a_link)
            mp3_list.append(mp3_link)
        
        # lấy link tiếp theo
        playlist = soup.find(class_="list-unstyled list_music sug_music")
        url = playlist.find('a')['href']    
        
        time.sleep(delay)
    return url