from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os
import requests
import time

# Download the following extensions with these commands:
# pip install selenium

apiLinks = ["A4:B55", "E4:F55", "I4:J55", "M4:N55", "Q4:R55"]

# Removes non critical bug with browser and Visual Studio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("headless")
driver = webdriver.Chrome( options = options)

# Gets current parent directory
cwd = Path(os.getcwd()).parent

# Gets code file path
codePath = str(cwd) + '/public/print_price_list/index.html'

# Checking for text on site
def checkForText(text):
    assert text in driver.find_element(By.XPATH, "/html/body").text

def TestProducts():
    driver.get(codePath)
    print("Loading site...")
    time.sleep(5)
    for dataColumns in apiLinks:
        response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Priser'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1408440166")
        productList = response.json()
        for product in productList["values"]:
            for item in product:
                checkForText(item)
                print('Found: ' + item)
    driver.close()
TestProducts()
print("Test successful!")