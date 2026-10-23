import os
from unittest import TestCase, main

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = "https://validator.w3.org/nu/"


class TestValidate(TestCase):
    doNotCloseBrowser = False
    hideWindow = True

    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.doNotCloseBrowser:
            chr_options.add_experimental_option("detach", True)

        if cls.hideWindow:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    def testValidation(self):
        # get all file paths
        paths = []

        for root, dirs, files in os.walk("./public", topdown=False):
            for name in files:
                paths.append(os.path.join(root, name))
            for name in dirs:
                paths.append(os.path.join(root, name))

        TABS_OPEN = 1
        failed_validations_count = 0

        # Loop through file paths and validate the files that ends with html or css
        for path in paths:
            if path.endswith(".html") or path.endswith(".css"):
                if "bootstrap" not in path:
                    # Open a new tab and switch to it
                    self.browser.execute_script("window.open('');")
                    TABS_OPEN += 1
                    self.browser.switch_to.window(
                        self.browser.window_handles[TABS_OPEN - 1]
                    )
                    # Open the validation website
                    self.browser.get(URL)
                    # Change dropdown to "file upload"
                    docselector = self.browser.find_element(By.ID, "docselect")
                    select = Select(docselector)
                    select.select_by_visible_text("file upload")
                    # Upload and submit file
                    self.browser.find_element(By.ID, "doc").send_keys(
                        os.path.abspath(path)
                    )
                    self.browser.find_element(By.ID, "submit").click()
                    try:
                        # Checks if messages filtering is available to see if a warning or error was found
                        self.browser.find_element(
                            By.XPATH, '//*[@id="filters"]/h2/button'
                        )
                    except NoSuchElementException:
                        continue
                    else:
                        failed_validations_count += 1

        # Writes out amount of files that failed validation
        if failed_validations_count > 0:
            self.fail(
                f"{failed_validations_count} files failed validation. See above for details."
            )


# Starts test if run as python file
if __name__ == "__main__":
    main(verbosity=2)
