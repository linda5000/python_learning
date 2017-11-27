from selenium import webdriver
import time

test_user = "linda5000"
test_pwd = "lindatest01"

browser = webdriver.Chrome()

# 打开www.lemfix.com
browser.get('http://www.lemfix.com')
time.sleep(1)

# 登录

# browser.find_element_by_xpath("//a[contains(text(), '登录')]").click()
browser.find_element_by_link_text('登录').click()
time.sleep(1)

# 用户名
username = browser.find_element_by_xpath("//input[@id='name']")
# 密码
password = browser.find_element_by_xpath("//input[@id='pass']")

username.clear()
username.send_keys(test_user)

time.sleep(1)

password.clear()
password.send_keys(test_pwd)

time.sleep(1)

# 点击登录
browser.find_element_by_xpath("//input[@type='submit']").click()

# 浏览器最大化
browser.maximize_window()

# 点击某一篇文章进行阅读
browser.find_element_by_xpath("//a[@class='topic_title']").click()

# 然后返回前一页
browser.back()
time.sleep(1)

# 利用forward返回到刚刚阅读的那篇文章
browser.forward()
time.sleep(1)

# 点击回复框
browser.find_element_by_xpath("//form[@id='reply_form']//div[@class='CodeMirror-scroll']").click()

# 输入回复内容
browser.find_element_by_xpath("//form[@id='reply_form']//div[contains(@class, 'CodeMirror')]//textarea").send_keys("6666")
time.sleep(1)

# 提交表单或点击回复按钮
browser.find_element_by_xpath("//form[@id='reply_form']").submit()
# browser.find_element_by_xpath("//form[@id='reply_form']//input[@type='submit']").click()


# 退出操作，关闭浏览器。
browser.close()
browser.quit()