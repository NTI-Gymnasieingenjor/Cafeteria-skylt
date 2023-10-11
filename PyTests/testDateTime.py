import time
from os import getcwd, path
from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTime(TestCase):
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

    def checkTime(self, date, result):
        self.browser.execute_script(f"startTime(new Date('{date}'));")
        shownTime = self.browser.find_element(By.ID, "clock").text
        self.assertEqual(shownTime, result)

    def testTime(self):
        # Monday
        self.checkTime("2023-05-08T09:00:00", "09:00")
        self.checkTime("2023-05-08T11:00:00", "11:00")
        self.checkTime("2023-05-08T13:00:00", "13:00")
        self.checkTime("2023-05-08T15:00:00", "15:00")

        # Tuesday
        self.checkTime("2023-05-09T09:00:00", "09:00")
        self.checkTime("2023-05-09T11:00:00", "11:00")
        self.checkTime("2023-05-09T13:00:00", "13:00")
        self.checkTime("2023-05-09T15:00:00", "15:00")

        # Wednesday
        self.checkTime("2023-05-10T09:00:00", "09:00")
        self.checkTime("2023-05-10T11:00:00", "11:00")
        self.checkTime("2023-05-10T13:00:00", "13:00")
        self.checkTime("2023-05-10T15:00:00", "15:00")

        # Thursday
        self.checkTime("2023-05-11T09:00:00", "09:00")
        self.checkTime("2023-05-11T11:00:00", "11:00")
        self.checkTime("2023-05-11T13:00:00", "13:00")
        self.checkTime("2023-05-11T15:00:00", "15:00")

        # Friday
        self.checkTime("2023-05-12T09:00:00", "09:00")
        self.checkTime("2023-05-12T11:00:00", "11:00")
        self.checkTime("2023-05-12T13:00:00", "13:00")
        self.checkTime("2023-05-12T15:00:00", "15:00")

        # Saturday
        self.checkTime("2023-05-13T09:00:00", "09:00")
        self.checkTime("2023-05-13T11:00:00", "11:00")
        self.checkTime("2023-05-13T13:00:00", "13:00")
        self.checkTime("2023-05-13T15:00:00", "15:00")

        # Sunday
        self.checkTime("2023-05-14T09:00:00", "09:00")
        self.checkTime("2023-05-14T11:00:00", "11:00")
        self.checkTime("2023-05-14T13:00:00", "13:00")
        self.checkTime("2023-05-14T15:00:00", "15:00")
