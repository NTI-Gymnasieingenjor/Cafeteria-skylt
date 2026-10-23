# !IMPORTANT!
# Run startServer.py before running this test

import unittest

from selenium.webdriver.common.by import By

from baseTestClass import BaseTestClass


class TestTemporaryClosed(BaseTestClass):
    website = "http://127.0.0.1:8000/?products=testProductList.csv&images=testImageList.csv&openHours=testOpenHoursListClosed.csv"

    def testTemporaryClosedSlidesCount(self):
        slides = self.browser.find_elements(By.CLASS_NAME, "carousel-item")
        # Only one slide should exist when temporary closed
        self.assertEqual(len(slides), 1)

    def testTemporaryClosedNotice(self):
        self.assertIn("tillfälligt stängt", self.browser.page_source)

    def testTemporaryClosedReason(self):
        self.assertIn("sjukdom", self.browser.page_source)


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()
