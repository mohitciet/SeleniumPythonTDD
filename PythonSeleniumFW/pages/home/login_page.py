from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from selenium import webdriver
import allure
from base.basepage import BasePage

class LoginPage(BasePage):

    ################
    ### Locators ###
    ################
    email_textbox_id="user_email"
    password_textbox_id = "user_password"
    login_button_name="commit"
    userIcon_label_xpath="//img[@class='ravatar']"
    invalidlogin_label_xpath="//div[contains(text(),'Invalid email or password')]"
    login_link_linkText = "Login"

    def __init__(self,driver):
        super().__init__( driver)
        self.driver=driver

    ############################
    ### Element Interactions ###
    ############################
    def login(self,username,password):
        self.clickElement(self.login_link_linkText,"link")
        self.sendKeys(username,self.email_textbox_id,"id")
        self.sendKeys(password,self.password_textbox_id, "id")
        self.clickElement(self.login_button_name,"name")

    def verifyLoginSuccessfull(self):
        return self.isElementPresent(self.userIcon_label_xpath,"xpath")

    def verifyLoginFailed(self):
        return self.isElementPresent(self.invalidlogin_label_xpath, "xpath")


