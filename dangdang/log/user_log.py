#coding = utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger_test = logging.getLogger()
        self.logger_test.setLevel(logging.DEBUG)
        #获取当前文件目录路径
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # print("base_dir:")
        # print(base_dir)
        log_dir = os.path.join(base_dir,"logs")
        # print("log_dir:")
        # print(log_dir)
        log_file = datetime.datetime.now().strftime("%Y-%m-%d" + ".logs")
        log_name = log_dir + "/" + log_file
        # print("log_name:")
        # print(log_name)

        #文件输出日志        
        # self.file_handle = logging.FileHandler(r"D:\pythonScript\imooc_chapter5\dangdang\log\logs\test.log")        
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s %(filename)s ---> %(funcName)s %(levelno)s %(levelname)s ------> %(message)s')
        self.file_handle.setFormatter(file_formatter)
        self.logger_test.addHandler(self.file_handle)
        self.logger_test.debug("test1234567890")

    def get_log(self):
        return self.logger_test

    def close_log(self):
        self.file_handle.close()
        self.logger_test.removeFilter(self.file_handle)

if __name__ == "__main__":
    user_l = UserLog()
#控制台输出日志
# consle = logging.StreamHandler()
# logger_test.addHandler(consle)
# logger_test.debug("test")
# consle.close()
# logger_test.removeHandler(consle)
