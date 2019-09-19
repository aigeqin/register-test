#coding = utf-8

import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")
from selenium import webdriver
from handle.register_handle import RegisterHandle
import time
import unittest

class RegisterBusiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_h = RegisterHandle(driver)

    # def login_input_test(self,phone):
    #     self.register_h.send_user_phone(phone)

    def login_input_data(self,phone,password,password_review,codetext):
        self.register_h.send_user_phone(phone)
        self.register_h.send_user_password(password)
        self.register_h.send_user_password_review(password_review)
        self.register_h.send_user_codetext(codetext)

    def login_click_button(self):
        self.register_h.click_accept_box()
        self.register_h.click_submit_button()

    def login_judgment(self,phone,password,password_review,codetext,assertCode, assertText):
        self.login_input_data(phone,password,password_review,codetext)        
        get_text = self.register_h.get_element_text(assertCode)
        get_text = get_text.strip(' ')
        assertText = assertText.strip(' ')
        # print("get_text = :")
        # print(get_text)
        # print("assertText = :"+assertText)
        if get_text == assertText:
            return True
        else:
            return False        

if __name__ == "__main__":
    register_b = RegisterBusiness(webdriver.Chrome())
    # register_b.login_input_test("12345")
    # register_b.login_input_data("13011112222","qinaige123","qinaige123","code123")
    test = register_b.login_judgment("13011112222","qinaige123","qinaige123","code123","code_text_error",u"验证码不正确，请重新填写")
    time.sleep(3)
    print(test)