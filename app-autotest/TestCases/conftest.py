import pytest
from appium import webdriver
from Public.read_config import ReadConfig
from PageObjects.login_page import  LoginPage
from TestData.common_data import *

@pytest.fixture
def init_driver():
    desired_caps = ReadConfig("phone.conf").getConfig("desired_caps","desired_caps")
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()