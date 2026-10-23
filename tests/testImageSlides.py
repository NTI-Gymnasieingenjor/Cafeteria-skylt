# !IMPORTANT!
# Run startServer.py before running this test

import unittest

from baseTestClass import BaseTestClass


class TestImageSlides(BaseTestClass):
    def testImagesPresent(self):
        self.assertIn("toast.png", self.browser.page_source)
        self.assertIn("danishPastry.png", self.browser.page_source)

    def testImagesHidden(self):
        self.assertNotIn("coffee.png", self.browser.page_source)
        self.assertNotIn("cinnamonBun.png", self.browser.page_source)


# Starts test if run as python file
if __name__ == "__main__":
    unittest.main()
