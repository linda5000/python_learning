from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from PageObjects.home_page_locator import *
import time
import re

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = Wait(self.driver,40,0.5)


    def get_nickname(self):
        self.wait.by_xpath(my_account_locator)
        link_name = self.driver.find_element_by_xpath(my_account_locator).text
        m = re.search(r'我的帐户\[(.*)\]', link_name)
        nickname = m.group(1)
        return nickname


    def bid_click(self):
        self.wait.by_xpath(bid_link_locator)
        self.driver.find_element_by_xpath(bid_link_locator).click()







