import logging

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
import logging as log


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerator.logGen()

    # Verifying HomePage Test
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******* Test_001_Login *******")
        self.logger.info("Verifying Home Page Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home Page Title Verified successfully")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("Home Page Title failed")
            assert False

    # Verifying LoginPage Test
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("Test_002_Login")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Create an Object of LoginPage
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.email)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("Login Page Verified failed")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_loginPage.png")
            self.driver.close()
            self.logger.info("Login Page Title failed")
            assert False


# if __name__ == "__main__":
#     logging.basicConfig(filename='./Logs/automation.log',
#                         format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S', level=log.INFO)
