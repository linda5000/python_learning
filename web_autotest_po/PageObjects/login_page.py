from selenium import webdriver
from web_autotest_po.Common.wait import Wait
from login_page_locator import *
import time

class LoginPage:
    def __init__(self,driver):
        self.driver = driver


    def login(self,url,user_value,pwd_value):
        self.driver.get(url)
        wait = Wait(self.driver,40,0.5)
        wait.by_xpath(user_locater)
        self.driver.find_element_by_xpath(user_locater).send_keys(user_value)
        time.sleep(1)
        self.driver.find_element_by_xpath(pwd_locater).send_keys(pwd_value)
        time.sleep(1)
        self.driver.find_element_by_xpath(submit_locater).click()



def main():
    user = "15815541763"
    pwd = "tudou111111"
    url = "http://120.76.42.189:8765/Index/login.html"
    browser = webdriver.Chrome()
    LoginPage(browser).login(url,user,pwd)



if __name__ == '__main__':
    main()



