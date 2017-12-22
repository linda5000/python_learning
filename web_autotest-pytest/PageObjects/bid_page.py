from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from PageObjects.bid_page_locator import *
import time

class BidPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = Wait(self.driver,40,0.5)


    def input_invest(self,amcount):
        self.wait.by_xpath(bid_investinput_locator)
        self.driver.find_element_by_xpath(bid_investinput_locator).send_keys(amcount)


    def click_investButton(self):
        self.wait.by_xpath(bid_button_locator)
        self.driver.find_element_by_xpath(bid_button_locator).click()


    def get_text_investButton(self):
        self.wait.by_xpath(bid_button_locator)
        return self.driver.find_element_by_xpath(bid_button_locator).text


    def get_investInputAmcount(self):
        self.wait.by_xpath(bid_investinput_locator)
        return self.driver.find_element_by_xpath(bid_investinput_locator).get_attribute("data-amount")

    def confirm_invest_sucess(self):
        self.wait.by_xpath(bid_layer_locator)
        self.driver.find_element_by_xpath(bid_invest_sucess_confirm_button_locator).click()


    def get_text_invest_errorinfo(self):
        self.wait.by_xpath(bid_layer_locator)
        return self.driver.find_element_by_xpath(bid_invest_fail_confirm_text_locator).text


    def confirm_invest_fail(self):
        self.wait.by_xpath(bid_layer_locator)
        self.driver.find_element_by_xpath(bid_invest_fail_confirm_button_locator).click()













