from __future__ import print_function
from selenium import webdriver
from pathlib import Path
import os
import requests

#Download the following extensions with these commands:
#pip install selenium

apiLinks = ["A4:B55", "E4:F55", "I4:J55", "M4:N55", "Q4:R55"]

# removes non critical bug with browser and visualstudio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome( options = options)

# gets current parent directory
cwd = Path(os.getcwd()).parent

# gets code file path way
codePath = str(cwd) + '/public/print_price_list/index.html'

# checking for text on site
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

def TestProducts():
    driver.get(codePath)
    for dataColumns in apiLinks:
        response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Priser'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1408440166")
        productList = response.json()
        print(productList)
        for product in productList["values"]:
            for item in product:
                print(item)
                checkForText(item)
    driver.close()
TestProducts()
print("Test successful!")