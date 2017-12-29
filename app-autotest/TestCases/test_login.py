from PageObjects.login_page import LoginPage
from PageObjects.home_page import  HomePage
from Common.global_path import image_path
from Common.logger import myLog
from TestData.login_data import *
from selenium import webdriver
import unittest
import time
import pytest



class TestLogin(unittest.TestCase):

    verificationErrors = []


    def setUp(self):
        myLog.info("TestLogin测试用例开始执行……")
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)


    def tearDown(self):
        self.driver.quit()
        myLog.info("TestLogin测试用例结束……")


    @pytest.mark.smoke
    def test_login_sucess(self):
        self.login_page.login(self.url,right_user,right_pwd)
        nickname = HomePage(self.browser).get_nickname()
        self.assertEqual(right_nickname,nickname)


    def test_login_noPwd(self):
        expectation = "请输入密码"
        self.login_page.login(self.url, right_user, "")
        error_info = self.login_page.pwd_error_info()
        self.assertEqual(expectation,error_info)



    def test_login_noPhone(self):
        expectation = "请输入手机号"
        self.login_page.login(self.url, "", "")
        error_info = self.login_page.phone_error_info()
        self.assertEqual(expectation, error_info)



    def test_login_errorPhone(self):
        expectation = "请输入正确的手机号"
        self.login_page.login(self.url, wrong_user, right_pwd)
        error_info = self.login_page.phone_error_info()
        self.assertEqual(expectation, error_info)


    def test_login_fail(self):
        expectation = "帐号或密码错误!"
        self.login_page.login(self.url, right_user, wrong_pwd)
        error_info = self.login_page.login_error_msg()
        self.assertEqual(expectation,error_info)


    def test_login_failtThird(self):
        expectation = "帐号或密码错误!"
        self.login_page.login(self.url, right_user, wrong_pwd)
        self.login_page.login(self.url, right_user, wrong_pwd)
        self.login_page.login(self.url, right_user, wrong_pwd)
        try:
            self.login_page.get_vcode()
        except Exception as e:
            self.browser.save_screenshot(image_path + "test_login-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))

        self.assertEqual([], self.verificationErrors)




