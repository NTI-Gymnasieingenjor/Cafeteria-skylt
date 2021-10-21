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

#Download with the command  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


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

    return final_result

print(Call_sheets_api())




# removes non critical bug with browser and visualstudio
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome( options = options)

# gets current parent directory
cwd = Path(os.getcwd()).parent

# gets code file path way
codePath = str(cwd) + '/public/index.html'

driver.get(codePath)

# checking for text on site
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

monday = True
tuesday = True
wednesday = True

if monday:
    monday_start = str(Call_sheets_api()[0] + " - " + Call_sheets_api()[1])
    monday_end = str(Call_sheets_api()[2] + " - " + Call_sheets_api()[3])
    print(monday_start)
    checkForText(monday_start)
    checkForText(monday_end)

elif tuesday:
    tuesday_start = str(Call_sheets_api()[4] + " - " + Call_sheets_api()[5])
    tuesday_end = str(Call_sheets_api()[6] + " - " + Call_sheets_api()[7])

elif wednesday:
    print()

driver.close()