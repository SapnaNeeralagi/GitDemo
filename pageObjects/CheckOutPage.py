from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import purchase


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    addtocart = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    confirm = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductsName(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def add(self):
        return self.driver.find_elements(*CheckOutPage.addtocart)

    def checknow(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def confirmnow(self):
        self.driver.find_element(*CheckOutPage.confirm).click()
        Purchase = purchase(self.driver)
        return Purchase



