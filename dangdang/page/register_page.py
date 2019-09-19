#coding = utf-8

import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")
from selenium import webdriver
from base.find_element import FindElement

class RegisterPage(object):
    def __init__(self,driver):
        self.find_e = FindElement(driver)
    #定位输入框，按钮    
    def get_phone_element(self):
        return self.find_e.get_element("phone")

    def get_password_element(self):
        return self.find_e.get_element("password")

    def get_password_review_element(self):
        return self.find_e.get_element("password_review")

    def get_code_text_element(self):
        return self.find_e.get_element("code_text")

    def get_accept_check_box_element(self):
        return self.find_e.get_element("accept_check_box")

    def get_submit_button_element(self):
        return self.find_e.get_element("submit_button")

    #错误元素定位
    def get_name_error_element(self):
        return self.find_e.get_element("name_error")
    def get_password_error_element(self):
        return self.find_e.get_element("password_error")
    def get_password_review_error_element(self):
        return self.find_e.get_element("password_review_error")
    def get_code_text_error_element(self):
        return self.find_e.get_element("code_text_error")
    def get_phone_error_element(self):
        return self.find_e.get_element("phone_error")
    
if __name__ == "__main__":
    register_p = RegisterPage(webdriver.Chrome())
    register_p.get_code_text_element().send_keys("130665")
