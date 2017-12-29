from selenium import webdriver
from Common.wait import Wait
from PageObjects.login_page_locator import *
import time

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        


# 输入手机号，点击下一步
    def input_phone(self,phone):
        self.driver.find_element_by_id(phone_locater).send_keys(phone)
        self.driver.find_element_by_id(button).click()


    def phone_error(self):
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout")
        self.driver.find_element_by_id ("com.xxzb.fenwoo:id/btn_confirm").click()


    def input_pwd(self,pwd):
        self.driver.find_element_by_id("com.xxzb.fenwoo:id/et_pwd").send_keys(pwd)
        self.driver.find_element_by_id(button).click()

    def pwd_error(self):
        return self.driver.find_element_by_id("com.xxzb.fenwoo:id/et_pwd").text



















