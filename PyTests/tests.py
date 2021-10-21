# -*- coding: utf-8 -*-
from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from pathlib import Path
import os

#Download the following extensions with these commands:
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#pip install selenium

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '../keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
spreadsheet_id = "1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ"
service = build('sheets', 'v4', credentials=credentials)


def Convert_to_usable_list(string):
    #Removes specified characters from the called string.
    disallowed_characters = '{[","]}'
    for character in string:
        for symbol in disallowed_characters:
            if character == symbol:
                string = string.replace(character, "")
    li = list(string.split(" "))
    del li[0:5]

    return li

def Call_sheets_api():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range="B4:E8").execute()
    listed_result = json.dumps(result)
    final_result = Convert_to_usable_list(listed_result)
    print(final_result)

    return final_result


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
    timeList = Call_sheets_api()

    for i in range(5):
        dayIndex = i * 4
        driver.execute_script("day = " + str(i + 1) + "; GetOpenHours();")
        time.sleep(1)

        day_start = str(timeList[dayIndex] + " - " + timeList[dayIndex+1])
        day_end = str(timeList[dayIndex+2] + " - " + timeList[dayIndex+3])
        print(day_start, i+1)
        checkForText(day_start)
        checkForText(day_end)


    driver.close()

TestWeekday()