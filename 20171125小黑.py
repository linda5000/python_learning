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
username.send_keys(test_user)

time.sleep(1)

password.clear()
password.send_keys(test_pwd)

time.sleep(1)

# 点击登录
browser.find_element_by_xpath("//button[@type='button']").click()

time.sleep(2)
browser.find_element_by_xpath("//div[@class='b-unit']//a[text()='抢投标']").click()

time.sleep(2)
browser.find_element_by_xpath("//input[@class='form-control invest-unit-investinput']").send_keys(1000)
time.sleep(1)

# 找到我的账户
browser.find_element_by_xpath("//a[contains(text(),'我的帐户')]").click()

locator = (By.XPATH, "//div[text()='投资项目']")
WebDriverWait(browser, 10, 0.5).until(EC.presence_of_element_located(locator))

browser.find_element_by_xpath("//div[text()='投资项目']").click()