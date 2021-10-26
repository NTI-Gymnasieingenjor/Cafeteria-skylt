# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from pathlib import Path
import os
import aiohttp
import asyncio

#Download the following extensions with these commands:
#pip install selenium
#pip install aiohttp



def ConvertToCleanList(string):
    #Removes specified characters from the called string.
    disallowedCharacters = '["] \n'
    for character in string:
        for symbol in disallowedCharacters:
            if character == symbol:
                string = string.replace(character, "")
    li = list(string.split(","))

    return li


async def main():
        #Function that gets the data from the sheet.
    async with aiohttp.ClientSession() as session:
        async with session.get('https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/B4:E8?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q') as response:
            html = await response.text()
            rawData = html[80:430]
            processedData = ConvertToCleanList(rawData)
    return processedData


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

def TestWeekday():
    driver.get(codePath)
    loop = asyncio.get_event_loop()
    timeList = loop.run_until_complete(main())
    

    for i in range(7):
        driver.execute_script("day = " + str(i + 1) + "; GetOpenHours();")
        time.sleep(1)
        if i <= 4:
            dayIndex = i * 4

            day_start = str(timeList[dayIndex] + " - " + timeList[dayIndex+1])
            day_end = str(timeList[dayIndex+2] + " - " + timeList[dayIndex+3])
            checkForText(day_start)
            checkForText(day_end)
        else:
            checkForText("Måndag - Fredag")
        
        driver.refresh()
    driver.close()

TestWeekday()