from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import Baseclass
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import purchase
from pageObjects.HomePage import HomePage


class TestOne(Baseclass):
    def test_e2e(self):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("Getting all the Titles of items")
        products = checkoutpage.getProductsName()

        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            log.info(productName)
            if productName == 'Blackberry':
                checkoutpage.add()[i].click()

        checkoutpage.checknow().click()

        addeditem = self.driver.find_element_by_link_text("Blackberry").text
        assert addeditem == 'Blackberry'

        Purchase = checkoutpage.confirmnow()
        log.info("Entering the Country Name")
        Purchase.purchaseclick().send_keys('ind')
        self.verifyTextPresence("India")
        Purchase.sendingText().click()
        Purchase.clickcheckbox().click()
        Purchase.finalstep().click()

        message = Purchase.successMessage().text
        log.info("Text received is"+message)
        assert "Success! Thank you!" in message