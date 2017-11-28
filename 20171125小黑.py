from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


url = "http://120.76.42.189:8765/Index/login.html"
test_user = "15815541763"
test_pwd = "tudou111111"

browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)


# 用户名
username = browser.find_element_by_xpath("//input[@name='phone']")
# 密码
password = browser.find_element_by_xpath("//input[@name='password']")

username.clear()
password.clear()

# 填写用户名和密码
username.send_keys(test_user)
time.sleep(1)
password.send_keys(test_pwd)
time.sleep(1)

# 点击登录
browser.find_element_by_xpath("//button[@type='button']").click()

# 浏览器最大化
browser.maximize_window()

time.sleep(2)

# 点击一个投标项目
name = ' 全栈一期web自动化测'
xpath = "//span[text()='%s']//ancestor::div[@class='b-unit']//a[text()='抢投标']"%name
browser.find_element_by_xpath(xpath).click()

time.sleep(2)

# 定位投标金额
browser.find_element_by_xpath("//input[@class='form-control invest-unit-investinput']").send_keys(1000)
time.sleep(1)

# 点击投标
xpath = "//button[text()='投标']"
# browser.find_element_by_xpath(xpath).click()

# 点击我的账户
browser.find_element_by_xpath("//a[contains(text(),'我的帐户')]").click()

# 点击投资项目
xpath = "//div[text()='投资项目']"
locator = (By.XPATH, xpath)
WebDriverWait(browser, 10, 1).until(EC.presence_of_element_located(locator))
browser.find_element_by_xpath(xpath).click()


# 根据某个特定时间找到对应的投标链接
date = '2017-11-28'
time = '10:05'
xpath = "//div[text()='%s']//following-sibling::div[text()='%s']//parent::td//following-sibling::td//div//a"%(date,time)
locator = (By.XPATH, xpath)
WebDriverWait(browser, 10, 1).until(EC.presence_of_element_located(locator))
browser.find_element_by_xpath(xpath).click()

# 退出操作，关闭浏览器。
# browser.close()
# browser.quit()
