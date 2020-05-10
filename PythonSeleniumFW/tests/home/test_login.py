from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import allure
from utilities.teststatus import TestStatus
import allure_commons


@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures("methodSetUp")
class TestLogin(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_Setup(self, methodSetUp):
        self.ll = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @allure.story('HCMAT-12345')
    @allure.title("Verify User is able to Login with Valid Credentials")
    @allure.tag('HCMAT-12345')
    @allure.description("Verify User is able to Login with Valid Credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.run(order=1)
    def test_validLogin(self):
        self.log.info("test_validLogin Test is started")
        self.ll.login("test@email.com","abcabc")
        result=self.ll.verifyLoginSuccessfull()
        self.ts.markFinal("test_validLogin",result,"User is not Able to Login")


    @allure.story('HCMAT-54574')
    @allure.tag('HCMAT-54574')
    @allure.title("Verify User is not able to Login with Invalid credentials")
    @allure.description("Verify User is not able to Login with Invalid credentials")
    @allure.severity(allure.severity_level.MINOR)
    #@pytest.mark.run(order=2)
    def test_invalidLogin(self):
        self.log.info("test_invalidLogin Test is started")
        self.ll.login("test1234@email.com","1234")
        result=self.ll.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "User Invalid Login")


