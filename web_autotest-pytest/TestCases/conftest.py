import pytest
from selenium import webdriver
from PageObjects.login_page import  LoginPage
from TestData.common_data import *

@pytest.fixture
def login_web():
    driver = webdriver.Chrome()
    driver.maximize_window()
    LoginPage(driver).login(url, phone, pwd)
    yield driver
    driver.close()
    driver.quit()