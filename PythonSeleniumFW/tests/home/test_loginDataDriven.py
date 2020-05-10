from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import allure
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import allure_commons


@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("methodSetUp")
@ddt
class TestLoginDataDriven(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_Setup(self, methodSetUp):
        self.ll = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)





    @allure.story('HCMAT-4545')
    @allure.tag('HCMAT-4545')
    @allure.title("Verify User is not able to Login with Data Driven Invalid credentials")
    @allure.description("Verify User is not able to Login with Data Driven Invalid credentials")
    @data(*getCSVData("D:\\PythonSeleniumFW\\testdata.csv"))
    @unpack
    @allure.severity(allure.severity_level.MINOR)
    def test_invalidLoginDataDriven(self,username,password):
        self.log.info("invalidLoginDataDriven Test is started")
        self.ll.login(username,password)
        result=self.ll.verifyLoginFailed()
        self.ts.markFinal("invalidLoginDataDriven", result, "User Invalid Login")


