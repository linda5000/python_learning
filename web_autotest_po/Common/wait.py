from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Wait:
    def __init__(self,driver,timeout,frequency):
        self.w = WebDriverWait(driver, timeout, frequency)

    def by_xpath(self,xpath):
        locator = (By.XPATH,xpath)
        self.w.until(EC.visibility_of_element_located(locator))
