from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()
driver.get('https://store.steampowered.com/search/?filter=topsellers&os=win')

items = []

last_height = driver.execute_script("return document.body.scrollHeight")

# itemTargetCount = 100

# while itemTargetCount > len(items):
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    # if itemTargetCount == len(items):
    #     break

    last_height = new_height

    games = driver.find_elements_by_class_name('responsive_search_name_combined')
    for game in games:
        name = game.find_element_by_xpath('.//*[@class="title"]').text
        price = game.find_element_by_css_selector('div.col.search_price.responsive_secondrow').text.replace("\u20ac", '')
        game_names_dict = {
            "name" : name,
            "price" : price
        }
        items.append(game_names_dict)

print(items)
print(len(items))

json.dump(items, open("items.json", "w"))

