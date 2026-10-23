# !IMPORTANT!
# Run startServer.py in terminal before running this test

import time
import unittest
from os import mkdir, path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from baseTestClass import BaseTestClass


class TestScreenshots(BaseTestClass):
    website = "http://127.0.0.1:8000"

    # Scrolls to every slide and saves a screenshot
    def testSaveScreenshot(self):
        # Gets number of slides on page
        nr_of_slides = len(self.browser.find_elements(By.CLASS_NAME, "carousel-item"))
        screenshot_nr = 1
        time.sleep(2)
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "carousel-item")
        )
        WebDriverWait(self.browser, 5).until(element_present)
        if not path.exists("screenshots/"):
            mkdir("screenshots/")
        for i in range(nr_of_slides):
            self.browser.save_screenshot(f"screenshots/slide{str(screenshot_nr)}.png")
            time.sleep(1)
            self.browser.execute_script("$('.carousel').carousel('next')")
            time.sleep(1)
            screenshot_nr += 1


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()
