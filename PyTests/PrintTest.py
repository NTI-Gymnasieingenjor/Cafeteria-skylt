from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import getcwd, path
from unittest import TestCase, main
import requests
import time

# Download the following extensions with these commands:
# pip install selenium

apiLinks = ["A4:B55", "E4:F55", "I4:J55", "M4:N55", "Q4:R55"]


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
        self.browser.get(path.join(getcwd(), "./public/print_price_list/index.html"))

    def tearDown(self):
        self.browser.get("about:blank")

    # Checking for text on site
    def checkForText(self, text):
        self.assertIn(text, self.browser.find_element(By.XPATH, "/html/body").text)

    def testProducts(self):
        print("Loading site...")
        time.sleep(5)
        for dataColumns in apiLinks:
            response = requests.get(
                "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Priser'!"
                + dataColumns
                + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1408440166"
            )
            productList = response.json()
            for product in productList["values"]:
                for item in product:
                    self.checkForText(item)
                    print("Found: " + item)
