#coding = utf-8
import sys
sys.path.append(r"D:\pythonScript\imooc_chapter4")
from selenium import webdriver
from handle.register_handle import RegisterHandle
import unittest

class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_case01(self):
        register_h = RegisterHandle(self.driver)
        register_h.send_user_base("qi","qinaige123","code123","13066983671")
        textinfo = "长度应为6~18个字符"
        text = register_h.get_element_text("name_error",textinfo)
        self.assertEqual(text,textinfo,"账号输入失败，验证成功")
        # self.assertNotEqual(text,textinfo,"账号输入成功，验证失败")
        print("测试完毕")
        
if __name__ == "__main__":
    unittest.main()



