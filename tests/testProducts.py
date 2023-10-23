# !IMPORTANT!
# Run startServer.py before running this test

import unittest
import csv

from selenium import webdriver

optionsChrome = webdriver.ChromeOptions()  # Define options for chrome
optionsChrome.add_argument("headless")  # Pass headless argument to the options (no ui)
browser = webdriver.Chrome(options=optionsChrome)

# Adress to website
website = "http://localhost:8000"
# Path to product list csv file
productListPath = "public/productList.csv"
# Resolution on screen
res = 1080, 1920

# Runs tests in Chrome
class TestProducts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.browser = browser
        browser.get(website)
        browser.set_window_size(*res)

    def testProductList(self):
        # Creates an array with the product data from the csv file
        menuList = []
        with open(productListPath, encoding='utf-8', newline='') as products:
            lines = csv.reader(products, delimiter=',', quotechar='|')
            for row in lines:
                menuList.append(row)
        # Checks if every item set to TRUE is in the page source code
        for categoryIndex in range(round(len(menuList)/4)):
            for itemIndex in range(len(menuList[2 + 4 * categoryIndex])):
                if menuList[2 + 4 * categoryIndex][itemIndex] == "TRUE":
                    self.assertIn(menuList[0 + 4 * categoryIndex][itemIndex], self.browser.page_source)

    # Closes the window after all the tests are done
    @classmethod
    def tearDownClass(self):
        self.browser.close()


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()