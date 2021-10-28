from __future__ import print_function
from selenium import webdriver
from pathlib import Path
import os
import requests
import time

#Download the following extensions with these commands:
#pip install selenium

apiLinks = ["A5:B55", "E5:F55", "I5:J55", "M5:N55"]
res = 1080, 1920

# removes non critical bug with browser and visualstudio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("headless")
driver = webdriver.Chrome( options = options)

# gets current parent directory
cwd = Path(os.getcwd()).parent

# gets code file path way
codePath = str(cwd) + '/public/index.html'

# checking for text on site
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

def TestProducts():
    driver.get(codePath)
    driver.set_window_size(*res)
    driver.execute_script("$('.carousel').carousel('prev')")
    print("Loading site...")
    time.sleep(1)
    for dataColumns in apiLinks:
        response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Datahantering'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1408440166")
        productList = response.json()
        for product in productList["values"]:
            for item in product:
                checkForText(item)
                print('Found: ' + item)
    driver.close()
TestProducts()
print("Test successful!")