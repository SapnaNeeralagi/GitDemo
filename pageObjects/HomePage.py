from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    submit = (By.XPATH, "//input[@type='submit']")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    msg = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clicksubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def selectcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getmsg(self):
        return self.driver.find_element(*HomePage.msg)
