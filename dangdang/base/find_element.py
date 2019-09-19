#coding = utf-8
import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")
from util.read_ini import ReadIni
from selenium import webdriver
import time
import os

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://login.dangdang.com/register.php?returnurl=http://myhome.dangdang.com/myOrder")

    def get_element(self,key):
        read_i = ReadIni()
        data = read_i.get_value(key)
        # print(data)
        element_by = data.split(' > ')[0]
        element_value = data.split(' > ')[1]
        # print(element_by + "\n")
        # print(element_value + "\n")
        try:
            if element_by == "id":
                return self.driver.find_element_by_id(element_value)
            elif element_by == "classname":
                return self.driver.find_element_by_class_name(element_value)
            elif element_by == "name":
                return self.driver.find_element_by_name(element_value)
            elif element_by == "xpath":
                return self.driver.find_element_by_xpath(element_value)
        except:
            save_path = os.path.join(os.getcwd()+"\\report\\"+"dangelementerror.png")
            self.driver.save_screenshot(save_path)
            return None

if __name__ == "__main__":
    find_e = FindElement(webdriver.Chrome())
    find_e.get_element("password").send_keys("13066998855")
    find_e.get_element("code_text").send_keys("code")
    time.sleep(3)    