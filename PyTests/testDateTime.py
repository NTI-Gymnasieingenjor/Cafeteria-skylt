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

    # A helper test for testTime
    def checkTime(self, date, result):
        # Runs startTime from main.js to change time
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

    # A helper test for testDate
    def checkDate(self, date, result):
        # Runs todaysDate from main.js to change date
        self.browser.execute_script(f"todaysDate(new Date('{date}'));")
        shownDate = self.browser.find_element(By.ID, "date").text
        self.assertEqual(shownDate, result)

    def testDate(self):
        # Monday
        self.checkDate("2023-05-08T00:00:00", "2023-05-08")
        self.checkDate("2023-05-08T08:00:00", "2023-05-08")
        self.checkDate("2023-05-08T15:45:00", "2023-05-08")
        self.checkDate("2023-05-08T23:59:00", "2023-05-08")

        # Tuesday
        self.checkDate("2023-05-09T00:00:00", "2023-05-09")
        self.checkDate("2023-05-09T08:00:00", "2023-05-09")
        self.checkDate("2023-05-09T15:45:00", "2023-05-09")
        self.checkDate("2023-05-09T23:59:00", "2023-05-09")

        # Wednesday
        self.checkDate("2023-05-10T00:00:00", "2023-05-10")
        self.checkDate("2023-05-10T08:00:00", "2023-05-10")
        self.checkDate("2023-05-10T15:45:00", "2023-05-10")
        self.checkDate("2023-05-10T23:59:00", "2023-05-10")

        # Thursday
        self.checkDate("2023-05-11T00:00:00", "2023-05-11")
        self.checkDate("2023-05-11T08:00:00", "2023-05-11")
        self.checkDate("2023-05-11T15:45:00", "2023-05-11")
        self.checkDate("2023-05-11T23:59:00", "2023-05-11")

        # Friday
        self.checkDate("2023-05-12T00:00:00", "2023-05-12")
        self.checkDate("2023-05-12T08:00:00", "2023-05-12")
        self.checkDate("2023-05-12T15:45:00", "2023-05-12")
        self.checkDate("2023-05-12T23:59:00", "2023-05-12")

        # Saturday
        self.checkDate("2023-05-13T00:00:00", "2023-05-13")
        self.checkDate("2023-05-13T08:00:00", "2023-05-13")
        self.checkDate("2023-05-13T15:45:00", "2023-05-13")
        self.checkDate("2023-05-13T23:59:00", "2023-05-13")

        # Sunday
        self.checkDate("2023-05-14T00:00:00", "2023-05-14")
        self.checkDate("2023-05-14T08:00:00", "2023-05-14")
        self.checkDate("2023-05-14T15:45:00", "2023-05-14")
        self.checkDate("2023-05-14T23:59:00", "2023-05-14")

    # A helper test for testWeekday
    def checkWeekday(self, date, result):
        # Runs todaysDate from main.js to change date
        self.browser.execute_script(f"todaysDate(new Date('{date}'));")
        shownWeekday = self.browser.find_element(By.ID, "day").text
        self.assertEqual(shownWeekday, result)

    def testWeekday(self):
        # Monday
        self.checkWeekday("2023-05-08T00:00:00", "Måndag")
        self.checkWeekday("2023-05-08T08:00:00", "Måndag")
        self.checkWeekday("2023-05-08T15:45:00", "Måndag")
        self.checkWeekday("2023-05-08T23:59:00", "Måndag")

        # Tuesday
        self.checkWeekday("2023-05-09T00:00:00", "Tisdag")
        self.checkWeekday("2023-05-09T08:00:00", "Tisdag")
        self.checkWeekday("2023-05-09T15:45:00", "Tisdag")
        self.checkWeekday("2023-05-09T23:59:00", "Tisdag")

        # Wednesday
        self.checkWeekday("2023-05-10T00:00:00", "Onsdag")
        self.checkWeekday("2023-05-10T08:00:00", "Onsdag")
        self.checkWeekday("2023-05-10T15:45:00", "Onsdag")
        self.checkWeekday("2023-05-10T23:59:00", "Onsdag")

        # Thursday
        self.checkWeekday("2023-05-11T00:00:00", "Torsdag")
        self.checkWeekday("2023-05-11T08:00:00", "Torsdag")
        self.checkWeekday("2023-05-11T15:45:00", "Torsdag")
        self.checkWeekday("2023-05-11T23:59:00", "Torsdag")

        # Friday
        self.checkWeekday("2023-05-12T00:00:00", "Fredag")
        self.checkWeekday("2023-05-12T08:00:00", "Fredag")
        self.checkWeekday("2023-05-12T15:45:00", "Fredag")
        self.checkWeekday("2023-05-12T23:59:00", "Fredag")

        # Saturday
        self.checkWeekday("2023-05-13T00:00:00", "Lördag")
        self.checkWeekday("2023-05-13T08:00:00", "Lördag")
        self.checkWeekday("2023-05-13T15:45:00", "Lördag")
        self.checkWeekday("2023-05-13T23:59:00", "Lördag")

        # Sunday
        self.checkWeekday("2023-05-14T00:00:00", "Söndag")
        self.checkWeekday("2023-05-14T08:00:00", "Söndag")
        self.checkWeekday("2023-05-14T15:45:00", "Söndag")
        self.checkWeekday("2023-05-14T23:59:00", "Söndag")
