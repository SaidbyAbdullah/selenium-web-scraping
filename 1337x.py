from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
# Headless mode
options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')


driver = webdriver.Chrome(options=options)
driver.get("https://1337x.to/")
driver.maximize_window()

time.sleep(1)
search_input = driver.find_element(By.NAME, 'search')
search_input.send_keys("titanic")
search_button = driver.find_element(By.XPATH, '//*[@id="search-index-form"]/button')
search_button.click()
time.sleep(1)

table_body = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div[1]/table/tbody')
torrent_titles = table_body.find_elements(By.XPATH, '//tr//td//a[2]')
torrent_title = []
for title in torrent_titles:
    torrent_title.append(title.text)

torrent_seeds = table_body.find_elements(By.XPATH, '//tr//td[contains(@class, "seeds")]')
torrent_seed = []
for seed in torrent_seeds:
    torrent_seed.append(seed.text)

torrent_leeches = table_body.find_elements(By.XPATH, '//tr//td[contains(@class, "leeches")]')
torrent_leech = []
for leech in torrent_leeches:
    torrent_leech.append(leech.text)

torrent_sizes = table_body.find_elements(By.XPATH, '//tr//td[contains(@class, "coll-4 size mob-")]')
torrent_size = []
for size in torrent_sizes:
    torrent_size.append(size.text)

torrent_uploaders = table_body.find_elements(By.XPATH, '//tr//td[contains(@class, "coll-5")]//a')
torrent_uploader = []
for uploader in torrent_uploaders:
    torrent_uploader.append(uploader.text)


df_torrents = pd.DataFrame({'title': torrent_title, 'size': torrent_size, 'seeds': torrent_seed, 'leechs': torrent_leech, 'uploader':torrent_uploader})
df_torrents.to_csv('1337x.csv', index=False)

