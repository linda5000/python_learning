from PageObjects.login_page import LoginPage
from selenium import webdriver
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        browser = webdriver.Chrome()


    def tearDown(self):
        browser.close()
        browser.quit()


    def test_login_sucess(self):
        LoginPage(browser)
