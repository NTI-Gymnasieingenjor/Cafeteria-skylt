# !IMPORTANT!
# Run startServer.py before running this test

import csv
import unittest

from selenium.webdriver.common.by import By

from baseTestClass import BaseTestClass


productListPath = "public/csv/openHoursList.csv"


class TestOpenHours(BaseTestClass):
    def testOpenHours(self):
        # Creates an array with the product data from the csv file
        menuList = []
        isClosed = False
        booleanCount = 0
        with open(productListPath, encoding="utf-8", newline="") as products:
            lines = csv.reader(products, delimiter=",", quotechar="|")
            for row in lines:
                menuList.append(row)
        # Check correct reason for closing if temporarily closed
        for categoryIndex in range(len(menuList)):
            for itemIndex in range(len(menuList[categoryIndex])):
                if menuList[categoryIndex][itemIndex] == "TRUE":
                    self.assertIn(
                        menuList[categoryIndex + 1][itemIndex],
                        self.browser.find_element(By.CLASS_NAME, "openHours").text,
                    )
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
                        self.assertIn(
                            menuList[categoryIndex][itemIndex + 1],
                            self.browser.find_element(By.ID, "openHours").text,
                        )
                    if menuList[categoryIndex][itemIndex] == "Efter lunch":
                        self.assertIn(
                            menuList[categoryIndex][itemIndex + 1],
                            self.browser.find_element(By.ID, "openHours").text,
                        )


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()
