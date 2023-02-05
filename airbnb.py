import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Headless mode
options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')


driver = webdriver.Chrome(options=options)
driver.get("https://www.airbnb.com/s/Karachi--Sindh--Pakistan/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Karachi%2C%20Sindh&place_id=ChIJv0sdZQY-sz4RIwxaVUQv-Zw&date_picker_type=calendar&checkin=2022-10-28&checkout=2022-10-31&adults=4&source=structured_search_input_header&search_type=autocomplete_click")
driver.maximize_window()
print("loading")
time.sleep(5)
print("loaded")
rooms_title = []
rooms_info = []
rooms_bed = []
rooms_bedroom = []
rooms_price = []
rooms_rating = []

room_titles = driver.find_elements(By.XPATH, '//div[contains(@class, "t1jojoys")]')
for room in room_titles:
    rooms_title.append(room.text)

room_infos = driver.find_elements(By.XPATH, '//div[contains(@class, "nquyp1l")]//span')
for room in room_infos:
    rooms_info.append(room.text)

room_beds = driver.find_elements(By.XPATH, '//div[contains(@class, "f15liw5s s1cjsi4j")]//span[1]//span')
for room in room_beds:
    rooms_bed.append(room.text)

room_bedrooms = driver.find_elements(By.XPATH, '//div[contains(@class, "f15liw5s s1cjsi4j")]//span[2]//span[3]')
for room in room_bedrooms:
    rooms_bedroom.append(room.text)

room_prices = driver.find_elements(By.XPATH, '//span[contains(@class, "_14y1gc")]//span[contains(@class, "_tyxjp1")]')
for room in room_prices:
    rooms_price.append(room.text + " per night")

room_ratingss = driver.find_elements(By.XPATH, '//span[contains(@class, "r1dxllyb")]')
for room in room_ratingss:
    rooms_rating.append(room.text)


df_rooms = pd.DataFrame({'title': rooms_title, 'info': rooms_info, 'beds': rooms_bed, 'bedrooms': rooms_bedroom, 'price': rooms_price, 'ratings': rooms_rating})

df_rooms.to_csv('airbnb.csv', index=False)