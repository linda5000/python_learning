from PageObjects.invest_page import InvestPage
from PageObjects.bid_page import BidPage
from PageObjects.home_page import  HomePage
from PageObjects.login_page import  LoginPage
from PageObjects.accountInfo_page import  AccountInfoPage
from Common.global_path import image_path
from Common.logger import myLog
from selenium import webdriver
import unittest
import datetime
import time



class TestInvest(unittest.TestCase):

    verificationErrors = []

    def setUp(self):
        myLog.info("TestInvest测试用例开始执行……")
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        LoginPage(self.browser).login("http://120.76.42.189:8765/Index/login.html","15815541763","tudou111111")
        HomePage(self.browser).bid_click()
        self.invest_page = InvestPage(self.browser)
        self.bidname = '全栈测试专用'


    def tearDown(self):
        self.browser.close()
        self.browser.quit()
        myLog.info("TestInvest测试用例执行结束……")



    def test_invest_sucess(self):
        before_amcount = float(self.invest_page.get_investInputAmcount_by_bidname(self.bidname))
        self.invest_page.investInput_by_bidname(self.bidname,100)
        self.invest_page.click_investButton_by_bidname(self.bidname)
        date = datetime.datetime.now()
        try:
            self.invest_page.confirm_invest_sucess()
        except Exception as e:
            self.browser.save_screenshot(image_path + "test_invest-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))


        accountInfo_page = AccountInfoPage(self.browser)
        accountInfo_page.click_investment_record()
        try:
            accountInfo_page.search_investment_record_by_time_bidname(date,self.bidname)
        except Exception as e:
            self.browser.save_screenshot(image_path + "test_invest-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))

        self.assertEqual([], self.verificationErrors)
        after_amcount = float(BidPage(self.browser).get_investInputAmcount())
        self.assertEqual(after_amcount,before_amcount - 100)



    def test_invest_wrongAmount1(self):
        self.invest_page.investInput_by_bidname(self.bidname, 1)
        error_info = self.invest_page.get_text_investButton_by_bidname(self.bidname)
        self.assertEqual("请输入10的整数倍",error_info)



    def test_invest_wrongAmount2(self):
        self.invest_page.investInput_by_bidname(self.bidname,20)
        self.invest_page.click_investButton_by_bidname(self.bidname)
        error_info = self.invest_page.get_text_invest_errorinfo()
        self.assertEqual("投标金额必须为100的倍数",error_info)





