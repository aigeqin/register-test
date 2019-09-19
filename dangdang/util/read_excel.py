#coding = utf-8
from xlutils.copy import copy
import xlrd

class ReadExcel(object):
    def __init__(self,excel_path = None, index = None):
        if excel_path == None:
            self.excel_path = r"D:\pythonScript\imooc_chapter5\dangdang\config\key_word.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0

        #打开文件，读取excel数据
        self.excel_data = xlrd.open_workbook(self.excel_path)
        #获取指定页签对象
        self.table_data = self.excel_data.sheets()[index]
   
    #获取行数
    def get_lines(self):
        lines = self.table_data.nrows
        if lines > 0:
            return lines
        return None


    #[[],[]]
    #获取每行数据，按照每行一个list,添加到一个大的list里面
    def get_sheet_data(self):
        sheet_data = []
        sheet_lines = self.get_lines()
        if sheet_lines != None:
            for i in range(sheet_lines):
                row_data = self.table_data.row_values(i)
                sheet_data.append(row_data)
                # print(row_data)
            return sheet_data 
        return None

    #获取每个单元格数据
    def get_cell(self,row,col):
        if row != None:
            cell_data = self.table_data.cell(row,col).value 
            return cell_data   
        return None

    #写入数据，传入行、列、值
    def write_value(self,row,col,value):        
        # read_value = self.excel_data
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)
    
if __name__ == "__main__":
    # third_c = ThirdCase(r"D:\pythonScript\imooc_chapter5\dangdang\config\key_word.xls")
    # print(tird_c.get_cell())
    # print(third_c.get_sheet_data())
    # third_c.write_value(9,1,"third_case")

    third_c2 = ReadExcel(index= 1)
    data = third_c2.get_sheet_data()
    print(data)