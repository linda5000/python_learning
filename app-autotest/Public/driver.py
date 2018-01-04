#coding=utf-8
from appium import webdriver

class Driver:

    def __init__(self,desired_caps):
        self.desired_caps=desired_caps

    def driver(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return driver

