from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import time
import unittest
import os

# Needs to have Chromedriver.exe in the same folder for the tests to work

optionsChrome = webdriver.ChromeOptions()  # Define options for chrome
optionsChrome.add_argument("headless")  # Pass headless argument to the options (no ui)
browser = webdriver.Chrome(options=optionsChrome)

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

website = parentPath + "\public\index.html"   # Website all test run on
print(website)
res = 1080, 1920

# Runs tests in Chrome
class TestChrome(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = browser
        self.browser.get(website)

    # Tests resolution and saves a screenshot
    def testSaveScreenshot(self):
        # Gets number of slides on page
        nr_of_slides = len(browser.find_elements_by_class_name("carousel-item"))
        print(nr_of_slides)

        screenshot_nr = 1
        self.browser.get(website)
        self.browser.set_window_size(*res)
        self.browser.execute_script("document.getElementById('weekend').classList.add('hidden');")
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'carousel-item'))
        WebDriverWait(self.browser, 5).until(element_present)
        for i in range(nr_of_slides):
            self.browser.save_screenshot("Slide" + str(screenshot_nr) + '.png')
            time.sleep(1)
            self.browser.execute_script("$('.carousel').carousel('next')")
            time.sleep(1)
            screenshot_nr = screenshot_nr + 1


    # Closes the window after all the tests are done
    @classmethod
    def tearDownClass(self):
        self.browser.close()

# Starts test
if __name__ == '__main__':
    unittest.main()

# Needs to have Chromedriver.exe in the same folder for the tests to work