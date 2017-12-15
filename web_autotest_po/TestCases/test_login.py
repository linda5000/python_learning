from PageObjects.login_page import LoginPage
from PageObjects.home_page import  HomePage
from Common.global_path import image_path
from Common.logger import myLog
from selenium import webdriver
import unittest
import time



class TestLogin(unittest.TestCase):

    verificationErrors = []

    def setUp(self):
        myLog.info("TestLogin测试用例开始执行……")
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)


    def tearDown(self):
        self.browser.close()
        self.browser.quit()
        myLog.info("TestLogin测试用例结束……")



    def test_login_sucess(self):
        user = "15815541763"
        pwd = "tudou111111"
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "土小姐"
        self.login_page.login(url,user,pwd)
        nickname = HomePage(self.browser).get_nickname()
        self.assertEqual(expectation,nickname)


    def test_login_noPwd(self):
        user = "15815541763"
        pwd = ""
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "请输入密码"
        self.login_page.login(url, user, pwd)
        error_info = self.login_page.pwd_error_info()
        self.assertEqual(expectation,error_info)



    def test_login_noPhone(self):
        user = ""
        pwd = ""
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "请输入手机号"
        self.login_page.login(url, user, pwd)
        error_info = self.login_page.phone_error_info()
        self.assertEqual(expectation, error_info)



    def test_login_errorPhone(self):
        user = "158"
        pwd = ""
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "请输入正确的手机号"
        self.login_page.login(url, user, pwd)
        error_info = self.login_page.phone_error_info()
        self.assertEqual(expectation, error_info)


    def test_login_fail(self):
        user = "15815541763"
        pwd = "***"
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "帐号或密码错误!"
        self.login_page.login(url, user, pwd)
        error_info = self.login_page.login_error_msg()
        self.assertEqual(expectation,error_info)


    def test_login_failtThird(self):
        user = "15815541763"
        pwd = "***"
        url = "http://120.76.42.189:8765/Index/login.html"
        expectation = "帐号或密码错误!"
        self.login_page.login(url, user, pwd)
        self.login_page.login(url, user, pwd)
        self.login_page.login(url, user, pwd)
        try:
            self.login_page.get_vcode()
        except Exception as e:
            self.browser.save_screenshot(image_path + "test_login-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))

        self.assertEqual([], self.verificationErrors)




