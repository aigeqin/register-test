#coding = utf-8
import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")
from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod(object):
    def __init__(self):
        pass
        # self.find_e = FindElement()
        # self.driver = driver

    def open_browser(self,browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome() 
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            print("请输入正确的浏览器")

    def get_url(self,url):
        self.driver.get(url)

    def get_element_action(self,key):
        fine_e = FindElement(self.driver)
        return fine_e.get_element(key)
        
    def send_value(self,value,key):
        self.get_element_action(key).send_keys(value)

    def click_element(self,key):
        self.get_element_action(key).click()

    def sleep_time(self):
        time.sleep(3)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

if __name__ == "__main__":
    action_m = ActionMethod()
    action_m.open_browser("Chrome")
    action_m.get_url("https://login.dangdang.com/register.php?returnurl=http://myhome.dangdang.com/myOrder")
    action_m.send_value("password","Mushishi")
    action_m.send_value("code_text","code")
    action_m.sleep_time()
    action_m.close_browser()
   