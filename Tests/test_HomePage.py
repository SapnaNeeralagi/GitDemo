import pytest

from TestData.HomePageData import Homepagedata
from Utilities.BaseClass import Baseclass
from pageObjects.HomePage import HomePage


class TestHomePage(Baseclass):

    def test_submitform(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First Name is"+getData["Firstname"])
        homepage.getName().send_keys(getData["Firstname"])
        log.info("First Name is" + getData["Lastname"])
        homepage.getEmail().send_keys(getData["Lastname"])
        homepage.getPassword().send_keys("Sapna@1992")
        homepage.selectcheckbox().click()
        self.genderValue(homepage.selectgender(), getData["Gender"])
        homepage.clicksubmit().click()
        message = homepage.getmsg().text
        self.screenshot("form.png")
        assert ("success" in message)

        self.driver.refresh()

    @pytest.fixture(params=Homepagedata.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
