# -*- coding: utf-8 -*-
from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json


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


monday = Call_sheets_api()

monday_start = monday[0]
monday_lunch_start = monday[1]

