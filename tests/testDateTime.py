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

    # A helper function for testClock
    def helperTestClock(self, date, result):
        # Runs getTime from main.js to change time
        self.browser.execute_script(f"getTime(new Date('{date}'));")
        shownTime = self.browser.find_element(By.ID, "clock").text
        self.assertEqual(shownTime, result)

    def testClock(self):
        self.helperTestClock("2023-05-08T09:00:00", "09:00")
        self.helperTestClock("2023-05-08T11:00:00", "11:00")
        self.helperTestClock("2023-05-08T18:00:00", "18:00")
        self.helperTestClock("2023-05-08T23:00:00", "23:00")
        self.helperTestClock("2023-05-08T08:35:14", "08:35")
        self.helperTestClock("2023-05-08T10:12:54", "10:12")
        self.helperTestClock("2023-05-08T12:54:12", "12:54")

    # A helper function for testDateAndWeekday
    def HelperTestDateAndWeekday(self, date, result, result2):
        # Runs getDate from main.js to change date
        self.browser.execute_script(f"getDate(new Date('{date}'));")
        shownDate = self.browser.find_element(By.ID, "date").text
        shownWeekday = self.browser.find_element(By.ID, "day").text
        self.assertEqual(shownDate, result)
        self.assertEqual(shownWeekday, result2)

    def testDateAndWeekday(self):
        # Monday
        self.HelperTestDateAndWeekday("2023-05-08T00:00:00", "2023-05-08", "Måndag")
        self.HelperTestDateAndWeekday("2023-05-08T08:00:00", "2023-05-08", "Måndag")
        self.HelperTestDateAndWeekday("2023-05-08T15:45:00", "2023-05-08", "Måndag")
        self.HelperTestDateAndWeekday("2023-05-08T23:59:00", "2023-05-08", "Måndag")

        # Tuesday
        self.HelperTestDateAndWeekday("2023-05-09T00:00:00", "2023-05-09", "Tisdag")
        self.HelperTestDateAndWeekday("2023-05-09T08:00:00", "2023-05-09", "Tisdag")
        self.HelperTestDateAndWeekday("2023-05-09T15:45:00", "2023-05-09", "Tisdag")
        self.HelperTestDateAndWeekday("2023-05-09T23:59:00", "2023-05-09", "Tisdag")

        # Wednesday
        self.HelperTestDateAndWeekday("2023-05-10T00:00:00", "2023-05-10", "Onsdag")
        self.HelperTestDateAndWeekday("2023-05-10T08:00:00", "2023-05-10", "Onsdag")
        self.HelperTestDateAndWeekday("2023-05-10T15:45:00", "2023-05-10", "Onsdag")
        self.HelperTestDateAndWeekday("2023-05-10T23:59:00", "2023-05-10", "Onsdag")

        # Thursday
        self.HelperTestDateAndWeekday("2023-05-11T00:00:00", "2023-05-11", "Torsdag")
        self.HelperTestDateAndWeekday("2023-05-11T08:00:00", "2023-05-11", "Torsdag")
        self.HelperTestDateAndWeekday("2023-05-11T15:45:00", "2023-05-11", "Torsdag")
        self.HelperTestDateAndWeekday("2023-05-11T23:59:00", "2023-05-11", "Torsdag")

        # Friday
        self.HelperTestDateAndWeekday("2023-05-12T00:00:00", "2023-05-12", "Fredag")
        self.HelperTestDateAndWeekday("2023-05-12T08:00:00", "2023-05-12", "Fredag")
        self.HelperTestDateAndWeekday("2023-05-12T15:45:00", "2023-05-12", "Fredag")
        self.HelperTestDateAndWeekday("2023-05-12T23:59:00", "2023-05-12", "Fredag")

        # Saturday
        self.HelperTestDateAndWeekday("2023-05-13T00:00:00", "2023-05-13", "Lördag")
        self.HelperTestDateAndWeekday("2023-05-13T08:00:00", "2023-05-13", "Lördag")
        self.HelperTestDateAndWeekday("2023-05-13T15:45:00", "2023-05-13", "Lördag")
        self.HelperTestDateAndWeekday("2023-05-13T23:59:00", "2023-05-13", "Lördag")

        # Sunday
        self.HelperTestDateAndWeekday("2023-05-14T00:00:00", "2023-05-14", "Söndag")
        self.HelperTestDateAndWeekday("2023-05-14T08:00:00", "2023-05-14", "Söndag")
        self.HelperTestDateAndWeekday("2023-05-14T15:45:00", "2023-05-14", "Söndag")
        self.HelperTestDateAndWeekday("2023-05-14T23:59:00", "2023-05-14", "Söndag")
