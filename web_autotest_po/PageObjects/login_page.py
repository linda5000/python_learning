from Common.Wait import Wait
import time

class LoginPage:
    def __init__(self,driver,u,p,u_value,p_value,submit):
        self.driver = driver
        self.u = u
        self.p = p
        self.u_value = u_value
        self.p_value = p_value
        self.submit = submit

    def login(self):
        wait = Wait(self.driver,40,0.5)
        wait.xpath(self.u)
        self.driver.find_element_by_xpath(self.u).send_keys(self.u_value)
        wait.xpath(self.p)
        self.driver.find_element_by_xpath(self.p).send_keys(self.p_value)
        wait.xpath(self.submit)
        self.driver.find_element_by_xpath(self.submit).click()







