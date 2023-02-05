import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Headless mode
options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')


driver = webdriver.Chrome()
driver.get("https://kickasstorrents.to/")
driver.maximize_window()

# search_bar = driver.find_element(By.ID, 'contentSearch')
# search_bar.send_keys("titanic")
# time.sleep(2)

torrent_containter = driver.find_element(By.XPATH, '//table[@class="doublecelltable"]//td//div//table[contains(@class, "frontPageWidget")]')
torrent_titles = torrent_containter.find_elements(By.XPATH, '//tr[@class="odd" or @class ="even"]//td//a')
torrent_title = []
for torrent in torrent_titles:
    torrent_title.append(torrent.text)

torrent_sizes = torrent_containter.find_elements(By.XPATH, '//tr[@class="odd" or @class ="even"]//td[contains(@class, "nobr")]')
torrent_size = []
for size in torrent_sizes:
    torrent_size.append(size.text)

torrent_uploaders = torrent_containter.find_elements(By.XPATH, '//tr[@class="odd" or @class ="even"]//td[@class="center"]')
torrent_uploader = []
for uploader in torrent_uploaders:
    torrent_uploader.append(uploader.text)

torrent_seeds = torrent_containter.find_elements(By.XPATH, '//tr[@class="odd" or @class ="even"]//td[contains(@class,"green")]')
torrent_seed = []
for seed in torrent_seeds:
    torrent_seed.append(seed.text)

torrent_leeches = torrent_containter.find_elements(By.XPATH, '//tr[@class="odd" or @class ="even"]//td[contains(@class,"lasttd")]')
torrent_leech = []
for leech in torrent_leeches:
    torrent_leech.append(leech.text)



df_torrents = pd.DataFrame({'title': torrent_title, 'size': torrent_size, 'seeds': torrent_seed, 'leechs': torrent_leech})
df_torrents.to_csv('kickasstorrents.csv', index=False)
