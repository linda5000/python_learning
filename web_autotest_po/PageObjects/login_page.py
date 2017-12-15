from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from PageObjects.login_page_locator import *
import time

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = Wait(self.driver,40,0.5)



    def login(self,url,user_value,pwd_value):
        self.driver.get(url)
        self.wait.by_xpath(user_locater)
        self.driver.find_element_by_xpath(user_locater).send_keys(user_value)
        time.sleep(1)
        self.driver.find_element_by_xpath(pwd_locater).send_keys(pwd_value)
        time.sleep(1)
        self.driver.find_element_by_xpath(submit_locater).click()


    def url(self):
        pass


    def phone_error_info(self):
        self.wait.by_xpath(phone_error_info_locator)
        return self.driver.find_element_by_xpath(phone_error_info_locator).text


    def pwd_error_info(self):
        self.wait.by_xpath(pwd_error_info_locator)
        return self.driver.find_element_by_xpath(pwd_error_info_locator).text


    def get_vcode(self):
        self.wait.by_xpath(vcode_locator)
        return self.driver.find_element_by_xpath(vcode_locator)

    def login_error_msg(self):
        self.wait.by_xpath(login_error_layer_locator)
        return self.driver.find_element_by_xpath(login_error_layer_locator).text
















