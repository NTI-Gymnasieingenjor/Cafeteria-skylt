from unittest import TestCase

from selenium import webdriver


class BaseTestClass(TestCase):
    doNotCloseBrowser = False
    hideWindow = True
    website = "http://127.0.0.1:8000/?products=testProductList.csv&images=testImageList.csv&openHours=testOpenHoursListOpen.csv"
    resolution = 1080, 1920

    @classmethod
    def setUpClass(cls):
        chromeOptions = webdriver.ChromeOptions()

        if cls.doNotCloseBrowser:
            chromeOptions.add_experimental_option("detach", True)

        if cls.hideWindow:
            chromeOptions.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chromeOptions)
        cls.browser.get(cls.website)
        cls.browser.set_window_size(*cls.resolution)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
