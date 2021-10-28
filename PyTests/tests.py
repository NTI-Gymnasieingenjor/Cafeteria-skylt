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

#Download the following extensions with these commands:
#pip install selenium


def TestProducts(apiLinks):
    driver.get(codePath)
    for dataColumns in apiLinks:
        response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Datahantering'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637")
        productList = response.json()
        print(productList)
        for product in productList["values"]:
            for item in product:
                print(item)
                checkForText(item)
    driver.close()


# removes non critical bug with browser and visualstudio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome( options = options)

# gets current parent directory
cwd = Path(os.getcwd()).parent

# gets code file path way
codePath = str(cwd) + '/public/index.html'

# checking for text on site
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

# tests that time is correct on Monday-Friday and that it's closed on weekends
def TestWeekdays(apiLinks):
    driver.get(codePath)
    loop = asyncio.get_event_loop()
    timeList = loop.run_until_complete(TestProducts(apiLinks))

    for i in range(0, 7):
        # sets the day in the javascript code
        driver.execute_script("day = " + str(i) + "; GetOpenHours();")
        time.sleep(1)
        # number 0 is sunday and 6 is saturday
        if i <= 5 and i > 0:
            # every fourth index in the list is a new day from the sheets
            dayIndex = (i - 1) * 2
            dayStart = str(timeList[dayIndex] + " - " + timeList[dayIndex+1])
            checkForText(dayStart)
        else:
            checkForText("Måndag - Fredag")

        driver.refresh()
    driver.close()

apiLinks = ["B4:C8", "A5:B55", "E5:F55", "M5:N55", "Q5:R55"]

TestWeekdays(apiLinks)