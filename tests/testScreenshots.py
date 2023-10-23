# !IMPORTANT!
# Run startServer.py in terminal before running this test

import os
import time
import unittest
from os import mkdir, path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

optionsChrome = webdriver.ChromeOptions()  # Define options for chrome
optionsChrome.add_argument("headless")  # Pass headless argument to the options (no ui)
browser = webdriver.Chrome(options=optionsChrome)

website = "http://localhost:8000"
res = 1080, 1920

# Runs tests in Chrome
class TestScreenshots(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.browser = browser
        browser.get(website)
        browser.get(website)
        browser.set_window_size(*res)

    # Scrolls to every slide and saves a screenshot
    def testSaveScreenshot(self):
        # Gets number of slides on page
        nr_of_slides = len(browser.find_elements(By.CLASS_NAME, "carousel-item"))
        screenshot_nr = 1
        time.sleep(2)
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "carousel-item")
        )
        WebDriverWait(self.browser, 5).until(element_present)
        if not path.exists("screenshots/"):
            mkdir("screenshots/")
        for i in range(nr_of_slides):
            self.browser.save_screenshot(f"screenshots/Slide{str(screenshot_nr)}.png")
            time.sleep(1)
            self.browser.execute_script("$('.carousel').carousel('next')")
            time.sleep(1)
            screenshot_nr += 1

    # Closes the window after all the tests are done
    @classmethod
    def tearDownClass(self):
        self.browser.close()


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()
