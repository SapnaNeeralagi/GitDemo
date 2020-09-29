import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyTextPresence(self, text):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def genderValue(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)
