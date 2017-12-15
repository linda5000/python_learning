from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from PageObjects.accountInfo_page_locator import *
import time,datetime

class AccountInfoPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = Wait(self.driver,40,0.5)


    def click_investment_record(self):
        self.wait.by_xpath(investment_record_locator)
        self.driver.find_element_by_xpath(investment_record_locator).click()



    def search_investment_record_by_time_bidname(self,date,bidname):
        day = date.strftime('%Y-%m-%d')
        time = date.strftime('%H:%M')
        self.wait.by_xpath(deal_mange_tab_locator)
        target = self.driver.find_element_by_xpath(deal_mange_tab_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.find_element_by_xpath(investment_link_locator%(day,time,bidname)).click()
















