# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
from pathlib import Path
import requests
import asyncio
from os import getcwd, path
from unittest import TestCase, main
from selenium.webdriver.common.by import By


# Download the following extensions with these commands:
# pip install selenium


class TestIndex(TestCase):
    doNotCloseBrowser = False
    hideWindow = True

    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if cls.doNotCloseBrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.browser.get(path.join(getcwd(), "./public/index.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    # Checking for text on site
    def testTitle(self):
        self.assertEqual("Prislista", self.browser.title)

    def checkForText(self, text):
        self.assertIn(text, self.browser.find_element(By.XPATH, "weekend").text)

    # Tests that time is correct on Monday-Friday and that it's closed on weekends
    def testWeekdays(self):
        print("Loading site...")
        response = requests.get(
            "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'%C3%96ppettider'!B4:C8?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q"
        )
        timeList = response.json()

        for i in range(0, 7):
            # Sets the day in the JavaScript code
            self.browser.execute_script("day = " + str(i) + "; getOpenHours();")
            time.sleep(1)
            # Number 0 is sunday and 6 is saturday
            if i <= 5 and i > 0:
                dayStart = str(
                    timeList["values"][i - 1][0] + " - " + timeList["values"][i - 1][1]
                )
                self.checkForText(dayStart)
            else:
                self.checkForText("Måndag - Fredag")
            print("Day " + str(i) + ": success")
            self.browser.refresh()


if __name__ == "__main__":
    main(verbosity=2)
