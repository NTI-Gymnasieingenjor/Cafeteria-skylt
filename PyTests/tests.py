# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from pathlib import Path
import os
import requests
import asyncio

# Download the following extensions with these commands:
# pip install selenium



# Removes non critical bug with browser and Visual Studio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome( options = options)

# Gets current parent directory
cwd = Path(os.getcwd()).parent

# Gets code file path way
codePath = str(cwd) + '/public/index.html'

# Checking for text on site
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

# Tests that time is correct on Monday-Friday and that it's closed on weekends
def TestWeekdays():
    driver.get(codePath)
    print("Loading site...")
    response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'%C3%96ppettider'!B4:C8?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q")
    timeList = response.json()

    for i in range(0, 7):
        # Sets the day in the JavaScript code
        driver.execute_script("day = " + str(i) + "; GetOpenHours();")
        time.sleep(1)
        # Number 0 is sunday and 6 is saturday
        if i <= 5 and i > 0:
            dayStart = str(timeList["values"][i-1][0] + " - " + timeList["values"][i-1][1])
            checkForText(dayStart)
        else:
            checkForText("Måndag - Fredag")
        print("Day " + str(i) + ": success")
        driver.refresh()
    driver.close()

TestWeekdays()
print("Test successful!")