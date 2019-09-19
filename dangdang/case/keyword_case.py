#coding = utf-8
import sys
sys.path.append(r"D:\pythonScript\imooc_chapter5\dangdang")

from util.read_excel import ReadExcel
from handlekeyword.action_method import ActionMethod

class KeywordCase(object):
    def run_main(self):
        self.action_m = ActionMethod()
        read_e = ReadExcel()
        case_lines = read_e.get_lines()
        is_run_col = 3
        if case_lines:
            for i in range(1,case_lines):
                read_e.write_value(i,10,"test")
                # continue
                handle_name = read_e.get_cell(i,2)
                print(handle_name+": ")
                is_run = read_e.get_cell(i,is_run_col)
                print(is_run)
                if is_run == "yes":
                    method = read_e.get_cell(i,4)
                    send_value = read_e.get_cell(i,5)
                    handle_value = read_e.get_cell(i,6)
                    except_result_method = read_e.get_cell(i,7)
                    except_result = read_e.get_cell(i,8)
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_excel_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                read_e.write_value(i,9,"pass")
                            else:
                                read_e.write_value(i,9,"fail")
                        elif except_value[0] == 'element':
                            print("except_value[1]:")
                            print(except_value[1])
                            print("except_result:")
                            print(except_result_method)
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                read_e.write_value(i,9,"pass")
                            else:
                                read_e.write_value(i,9,"fail")
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")

    def get_excel_result_value(self,data):
        return data.split(" = ")

    def run_method(self,method,send_value = '',handle_value = ''):
        method_value = getattr(self.action_m,method)
        if send_value != '' and handle_value != '':
            result = method_value(send_value,handle_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        elif send_value == '' and handle_value != '':
            result = method_value(handle_value)
        else:
            result = method_value()
        return result
 
if __name__ == "__main__":
    keyword_c = KeywordCase()
    keyword_c.run_main()

