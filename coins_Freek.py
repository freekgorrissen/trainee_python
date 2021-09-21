import pandas as pd ## tabel package
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""Scraping stuff"""
URL = 'https://coinmarketcap.com/'
driver_path = "C:/Users/fgorr/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get(URL)
time.sleep(3) # wait 3 seconds for initial page to load

scroll_height = driver.execute_script("return document.body.scrollHeight;")
screen_height = driver.execute_script("return window.screen.height;")

# Loop to scroll through the page
i = 1
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(1) # wait 1 second for page to load
    if screen_height * i > scroll_height: # stop when bottom of screen is reached
        break

# Create soup, find all table elements.
soup = BeautifulSoup(driver.page_source, 'html.parser') # Create soup using the URL from driver
tabel = soup.find('tbody')
rijen = tabel.find_all('tr')


class Coin:
    naam = ""
    prijs = -1

beleggingen = []


# Loop over all table elements (rows) and find prijs and naam for each coin
i = 0
while True:
    try:
        belegging = Coin()
        titel = rijen[i].find_all('p')
        belegging.naam = titel[1].text
        prijs = rijen[i].find_all('a')
        belegging.prijs = prijs[1].text
        beleggingen.append(belegging)
        i += 1
    except:
        print("aantal rijen: " + str(len(rijen)))
        print("aantal gescraped: " + str(len(beleggingen)))
        break


for b in beleggingen[0:10]:
    print(b.naam)
    print(b.prijs)

