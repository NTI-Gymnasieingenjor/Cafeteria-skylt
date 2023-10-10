from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from unittest import TestCase, main
from os import getcwd, path
from pathlib import Path
import requests
import time

# Download the following extensions with these commands:
# pip install selenium

apiLinks = ["A5:B55", "E5:F55", "I5:J55", "M5:N55"]
res = 1080, 1920

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
    def checkForText(self,text):
        self.assertIn(self.browser.find_element(By.XPATH, "/html/body").text, text)

    def testProducts(self):
        self.browser.set_window_size(*res)
        self.browser.execute_script("$('.carousel').carousel('prev')")
        print("Loading site...")
        time.sleep(1)
        for dataColumns in apiLinks:
            response = requests.get("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Datahantering'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1408440166")
            productList = response.json()
            for product in productList["values"]:
                for item in product:
                    self.checkForText(item)
                    print('Found: ' + item)
