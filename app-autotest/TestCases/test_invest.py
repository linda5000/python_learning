from PageObjects.invest_page import InvestPage
from PageObjects.bid_page import BidPage
from PageObjects.home_page import  HomePage
from PageObjects.accountInfo_page import  AccountInfoPage
from Common.global_path import image_path
from Public.logger import myLog
from TestData.common_data import *
from TestData.invest_data import *
import unittest
import datetime
import time
import pytest

# @pytest.mark.usefixtures("login_web")
class TestInvest():

    verificationErrors = []

    # @pytest.mark.smoke
    def test_invest_sucess(self,login_web):
        LoginPage(login_web).login_click()
        invest_page = InvestPage(login_web)
        before_amcount = float(invest_page.get_investInputAmcount_by_bidname(bidname))
        invest_page.investInput_by_bidname(bidname,right_amcount)
        invest_page.click_investButton_by_bidname(bidname)
        date = datetime.datetime.now()
        try:
            invest_page.confirm_invest_sucess()
        except Exception as e:
            login_web.save_screenshot(image_path + "test_invest-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))


        accountInfo_page = AccountInfoPage(login_web)
        accountInfo_page.click_investment_record()
        try:
            accountInfo_page.search_investment_record_by_time_bidname(date,bidname)
        except Exception as e:
            login_web.save_screenshot(image_path + "test_invest-" + time.strftime('%Y_%m_%d_%H_%M_%S') + "-error.png")
            self.verificationErrors.append(e)
            myLog.exception(str(e))

        assert not self.verificationErrors
        after_amcount = float(BidPage(login_web).get_investInputAmcount())
        assert after_amcount == before_amcount - right_amcount



    def test_invest_wrongAmount1(self,login_web):
        HomePage(login_web).bid_click()
        invest_page = InvestPage(login_web)
        invest_page.investInput_by_bidname(bidname, wrong_amcount1)
        error_info = invest_page.get_text_investButton_by_bidname(bidname)
        assert error_info == "请输入10的整数倍"



    def test_invest_wrongAmount2(self,login_web):
        HomePage(login_web).bid_click()
        invest_page = InvestPage(login_web)
        invest_page.investInput_by_bidname(bidname,wrong_amcount2)
        invest_page.click_investButton_by_bidname(bidname)
        error_info = invest_page.get_text_invest_errorinfo()
        assert error_info == "投标金额必须为100的倍数"





