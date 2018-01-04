from PageObjects.login_page import LoginPage
from Common.global_path import image_path
from Public.logger import myLog
from TestData.login_data import *
import time
import pytest


@pytest.mark.usefixtures("init_driver")
class TestLogin():

    verificationErrors = []

    @pytest.mark.smoke
    def test_login_sucess(self,init_driver):
        LP = LoginPage(init_driver)
        LP.login_click()
        LP.input_phone(right_phone)
        LP.input_pwd(right_pwd)

    def test_login_noPhone(self):
        expectation = "请输入手机号"
        self.login_page.login(self.url, "", "")
        error_info = self.login_page.phone_error_info()
        self.assertEqual(expectation, error_info)

    def test_login_noPwd(self):
        expectation = "请输入密码"
        self.login_page.login(self.url, right_user, "")
        error_info = self.login_page.pwd_error_info()
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




