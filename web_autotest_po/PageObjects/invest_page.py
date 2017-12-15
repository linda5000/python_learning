from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from PageObjects.invest_page_locator import *
import time

class InvestPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = Wait(self.driver,40,0.5)


    def click_bidname(self,bidname):
        self.wait.by_xpath(bid_link_locator%bidname)
        self.driver.find_element_by_xpath(bid_link_locator%bidname).click()


    def investInput_by_bidname(self,bidname,amcount):
        self.wait.by_xpath(bid_investinput_locator%bidname)
        self.driver.find_element_by_xpath(bid_investinput_locator%bidname).send_keys(amcount)


    def click_investButton_by_bidname(self,bidname):
        self.wait.by_xpath(bid_button_locator%bidname)
        self.driver.find_element_by_xpath(bid_button_locator%bidname).click()


    def get_text_investButton_by_bidname(self,bidname):
        self.wait.by_xpath(bid_button_locator%bidname)
        return self.driver.find_element_by_xpath(bid_button_locator%bidname).text


    def get_investInputAmcount_by_bidname(self,bidname):
        self.wait.by_xpath(bid_investinput_locator%bidname)
        return self.driver.find_element_by_xpath(bid_investinput_locator%bidname).get_attribute("data-amount")

    def confirm_invest_sucess(self):
        self.wait.by_xpath(bid_layer_locator)
        self.driver.find_element_by_xpath(bid_invest_sucess_confirm_button_locator).click()


    def get_text_invest_errorinfo(self):
        self.wait.by_xpath(bid_layer_locator)
        return self.driver.find_element_by_xpath(bid_invest_fail_confirm_text_locator).text


    def confirm_invest_fail(self):
        self.wait.by_xpath(bid_layer_locator)
        self.driver.find_element_by_xpath(bid_invest_fail_confirm_button_locator).click()













