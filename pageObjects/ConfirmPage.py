from selenium.webdriver.common.by import By


class purchase:

    def __init__(self, driver):
        self.driver = driver

    purchaseitem = (By.ID, "country")
    sendtext = (By.LINK_TEXT, "India")
    box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    finalcheckout = (By.XPATH, "//input[@value='Purchase']")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def purchaseclick(self):
        return self.driver.find_element(*purchase.purchaseitem)

    def sendingText(self):
        return self.driver.find_element(*purchase.sendtext)

    def clickcheckbox(self):
        return self.driver.find_element(*purchase.box)

    def finalstep(self):
        return self.driver.find_element(*purchase.finalcheckout)

    def successMessage(self):
        return self.driver.find_element(*purchase.message)
