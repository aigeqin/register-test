#coding = utf-8

import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")
from selenium import webdriver
from log.user_log import UserLog
import unittest
import ddt
import os
import HTMLTestRunner
from business.register_business import RegisterBusiness
import time
from util.read_excel import ReadExcel

log = UserLog()
logger = log.get_log()

read_ex = ReadExcel(r"D:\pythonScript\imooc_chapter5\dangdang\config\case_data.xls")
data = read_ex.get_sheet_data()
@ddt.ddt
class SecondCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()  

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://login.dangdang.com/register.php?returnurl=http://myhome.dangdang.com/myOrder")
        self.register_b = RegisterBusiness(self.driver)
        self.logger.info("这。。。This is Chrome, second_case test")
    
    def tearDown(self):
        # time.sleep(1)
        for error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                # case_name = self._testMethodDoc
                file_path = os.path.join(os.getcwd()+"\\dangdang\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        log.close_log()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_log()

    @ddt.data(*data)
    def test_register_login(self,data):
        phone,password,password_review,codetext,assertCode,assertText = data
        # self.register_b.login_input_data(name,password,password_review,codetext,phone)
        just_result = self.register_b.login_judgment(phone,password,password_review,codetext,assertCode,assertText)
        self.assertTrue(just_result,"检测到error信息，case执行")

if __name__ == "__main__":
    # file_path = os.path.join(os.getcwd()+"/dangdang/report/"+"secondcase.html")
    file_path = r"D:\pythonScript\imooc_chapter5\dangdang\report\secondcase.html"
    f = open(file_path,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(SecondCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is dangdang report",
    description="这是dangdang注册的的测试报告",verbosity=2)
    runner.run(suite)