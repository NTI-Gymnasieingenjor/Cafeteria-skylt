# !IMPORTANT!
# Run startServer.py before running this test

import csv
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

optionsChrome = webdriver.ChromeOptions()  # Define options for chrome
optionsChrome.add_argument("headless")  # Pass headless argument to the options (no ui)
browser = webdriver.Chrome(options=optionsChrome)

# Adress to website
website = "http://localhost:8000"
# Path to product list csv file
productListPath = "public/openHoursList.csv"
# Resolution on screen
res = 1080, 1920

# Runs tests in Chrome
class TestOpenHours(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.browser = browser
        browser.get(website)
        browser.set_window_size(*res)

    def testOpenHours(self):
        # Creates an array with the product data from the csv file
        menuList = []
        isClosed = False
        booleanCount = 0
        with open(productListPath, encoding='utf-8', newline='') as products:
            lines = csv.reader(products, delimiter=',', quotechar='|')
            for row in lines:
                menuList.append(row)
        # Check correct reason for closing if temporarily closed
        for categoryIndex in range(len(menuList)):
            for itemIndex in range(len(menuList[categoryIndex])):
                if menuList[categoryIndex][itemIndex] == "TRUE":
                    self.assertIn(menuList[categoryIndex + 1][itemIndex], self.browser.find_element(By.CLASS_NAME,'openHours').text)
                    isClosed = True
                    booleanCount += 1
                if menuList[categoryIndex][itemIndex] == "FALSE":
                    booleanCount += 1
        # Check that there is only one TRUE or FALSE in csv file
        self.assertEqual(booleanCount, 1)
        # If not closed, check the correct time is displayed
        if isClosed == False:
            for categoryIndex in range(len(menuList)):
                for itemIndex in range(len(menuList[categoryIndex])):
                    if menuList[categoryIndex][itemIndex] == "Före lunch":
                        self.assertIn(menuList[categoryIndex][itemIndex + 1], self.browser.find_element(By.ID,'openHours').text)
                    if menuList[categoryIndex][itemIndex] == "Efter lunch":
                        self.assertIn(menuList[categoryIndex][itemIndex + 1], self.browser.find_element(By.ID,'openHours').text)

    # Closes the window after all the tests are done
    @classmethod
    def tearDownClass(self):
        self.browser.close()


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()