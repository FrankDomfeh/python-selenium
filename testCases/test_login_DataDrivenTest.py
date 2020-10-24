import logging
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities import ExcelUtils
import logging


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL() # Getting the URL from ini file and readProperties
    path = "./TestData/LoginData.xlsx"   # Specify the path for the xl data
    logger = LogGenerator.logGen()

    # Verifying LoginPage Test
    @pytest.mark.regression
    def test_DDT_loginPage(self, setup):
        self.logger.info("******* Test_002__DDT_Login *******")
        self.logger.info("******** Verifying Login DDT test ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        # Create an Object of LoginPage
        self.login = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in the Excel:", self.rows)

        list_status = []  # Empty list

        # 2 specifies the 2nd row in the excel sheet
        # rows+1 specifies the number of rows + the last row
        for r in range(2, self.rows+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.userPassword = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.login.setUsername(self.user)
            self.login.setPassword(self.userPassword)
            self.login.clickLogin()

            # Getting the title of the page
            act_title = self.driver.title
            exp_tile = "Dashboard / nopCommerce administration"

            # comparing if actual title is equal to expected title
            if act_title == exp_tile:
                if self.expected == "Pass":  # checking if exp matches xl data "pass"
                    self.logger.info("****** Pass *****")
                    time.sleep(5)
                    self.login.clickLogout();
                    list_status.append("Pass")
                elif self.expected == "Fail":  # checking if exp matches xl data "pass"
                    self.logger.info("***** failed *****")
                    time.sleep(3)
                    self.login.clickLogout();
                    list_status.append("Fail")
            elif act_title != exp_tile:
                if self.expected == "Pass":
                    self.logger.info("***** failed ******")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("**** Passed ******")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***** Login DDT test passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test failed *****")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test ******")
        self.logger.info("******* Completed TC_LoginDDT_002 *******")

